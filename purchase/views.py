from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from debt.models import Debt
from debt.permissions import IsNotSuperuser
from links.models import Link
from product.models import Product
from purchase.models import Purchase
from purchase.paginators import PurchasePagination
from purchase.serializers import PurchaseSerializer


class PurchaseCreateAPIView(generics.CreateAPIView):
    """
    Контроллер закупки продуктов/товаров.
    """
    model = Purchase
    serializer_class = PurchaseSerializer

    def perform_create(self, serializer):

        product_id = self.request.data.get('product_name')  # получение id продукта
        supplier = self.request.data.get('supplier')  # продавец/владелец
        buyer = self.request.data.get('buyer')  # покупатель
        link_instance = Link.objects.get(pk=buyer)
        city = link_instance.city  # город
        country = link_instance.country  # страна
        total_quantity = self.request.data.get('quantity')  # количество закупаемого товара
        product = get_object_or_404(Product, id=product_id, owner_link=supplier)

        if product:
            hierarchy = product.hierarchy  # иерархия
            price = product.price  # цена товара
            quantity_to_purchase = product.quantity  # общее количество товара у поставщика

            if quantity_to_purchase >= total_quantity:
                remaining_quantity = quantity_to_purchase - total_quantity
                product.quantity = remaining_quantity
                product.save()

                if hierarchy < 2:
                    hierarchy = hierarchy + 1
                else:
                    hierarchy = 2

                debt = total_quantity * price  # сумма покупки

                data = {
                    'duty': debt,
                    'borrower': Link(pk=supplier),
                    'debtor': Link(pk=buyer),
                    'product': product,
                    'owner': self.request.user  # экземпляр модели User
                }

                Debt.objects.create(**data)

                parameters = {
                    'name': product.name,  # название
                    'model': product.model,  # модель
                    'price': product.price,  # цена
                    'quantity': total_quantity,  # количество
                    'release_date': product.release_date,  # дата выхода на рынок
                    'supplier': Link(pk=supplier),  # поставщик
                    'owner_link': Link(pk=buyer),  # владелец
                    'hierarchy': hierarchy,  # иерархия
                    'city': city,  # город
                    'country': country
                }

                Product.objects.create(**parameters)  # запись в БД закупки товара
                owner = self.request.user
                serializer.save(owner=owner)
            else:
                return JsonResponse({'error': 'Недостаточно товара на складе'}, status=400)

        else:
            return JsonResponse({'error': 'Продукт не найден'}, status=404)


class PurchaseListAPIView(generics.ListAPIView):
    """
    Контроллер списка закупок продуктов/товаров.
    """
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()
    pagination_class = PurchasePagination

    def get_queryset(self):
        # получаем базовый набор объектов из родительского класса.
        queryset = super().get_queryset()
        # фильтруем объекты, оставляя те, которые принадлежат текущему пользователю.
        queryset = queryset.filter(owner=self.request.user)
        return queryset


class PurchaseRetrieveAPIView(generics.RetrieveAPIView):
    """
    Контроллер просмотра закупки.
    """

    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()


class PurchaseDestroyAPIView(generics.DestroyAPIView):
    """
    Контроллер удаления закупки.
    """

    queryset = Purchase.objects.all()
    permission_classes = [IsNotSuperuser]
