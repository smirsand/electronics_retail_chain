from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics

from debt.models import Debt
from links.models import Link
from product.models import Product
from purchase.models import Purchase
from purchase.serializers import PurchaseSerializer


class PurchaseCreateAPIView(generics.CreateAPIView):
    """
    Контроллер закупки продуктов/товаров.
    """
    model = Purchase
    serializer_class = PurchaseSerializer

    def perform_create(self, serializer):
        print(serializer)
        product_id = self.request.data.get('product_name')  # получение id продукта
        total_quantity = self.request.data.get('quantity')  # количество закупаемого товара
        product = get_object_or_404(Product, id=product_id)  # получение параметров продукта по id
        hierarchy = product.hierarchy  # иерархия
        price = product.price  # цена товара
        quantity_to_purchase = product.quantity  # общее количество товара у поставщика

        supplier = self.request.data.get('supplier')  # продавец/владелец
        buyer = self.request.data.get('buyer')  # покупатель
        print(buyer)
        print(supplier)
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
                'product': product_id
            }

            Debt.objects.create(**data).save()  # запись задолженности в БД

            parameters = {
                'name': product.name,  # название
                'model': product.model,  # модель
                'price': product.price,  # цена
                'quantity': total_quantity,  # количество
                'release_date': product.release_date,  # дата выхода на рынок
                'supplier': Link(pk=supplier),  # поставщик
                'owner': Link(pk=buyer),  # владелец
                'hierarchy': hierarchy,  # иерархия
            }

            Product.objects.create(**parameters)  # запись в БД закупки товара
            serializer.save()
        else:
            message = {'error': 'Выберите меньшее количество!'}
            return JsonResponse(message, status=400)


class PurchaseListAPIView(generics.ListAPIView):
    """
    Контроллер списка закупок продуктов/товаров.
    """
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()
