from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from links.models import Link
from product.models import Product
from purchase.models import Purchase
from purchase.serializers import PurchaseSerializer


# class PurchaseProduct(APIView):
#     def post(self, request, product_id, new_owner_id):
#         product = get_object_or_404(Product, id=product_id)
#         new_owner = get_object_or_404(Link, id=new_owner_id)
#
#         # Создать новый товар с новым владельцем
#         new_product = Product.objects.create(
#             name=product.name,
#             model=product.model,
#             price=product.price,
#             quantity=product.quantity,
#             release_date=product.release_date,
#             supplier=product.supplier,
#             owner=new_owner
#         )
#
#         # теперь новый продукт принадлежит новому владельцу,
#         # а старый продукт остается неизменным
#
#         return Response("Товар успешно закуплен.")


class PurchaseCreateAPIView(generics.CreateAPIView):
    """
    Контроллер закупки продуктов/товаров.
    """
    model = Purchase
    serializer_class = PurchaseSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        product_id = self.request.data.get('product_name')
        product = Product.objects.get(id=product_id)
        hierarchy = product.hierarchy  # иерархия
        supplier = self.request.data.get('supplier')  # продавец/владелец
        buyer = self.request.data.get('buyer')  # покупатель

        if hierarchy < 2:
            hierarchy = hierarchy + 1
        else:
            hierarchy = 2

        # Получение всех параметров
        parameters = {
            'name': product.name,  # название
            'model': product.model,  # модель
            'price': product.price,  # цена
            'quantity': product.quantity,  # количество
            'release_date': product.release_date,  # дата выхода на рынок
            'supplier': Link(pk=supplier),  # поставщик
            'owner': Link(pk=buyer),  # владелец
            'hierarchy': hierarchy,  # иерархия
        }

        new_product = Product.objects.create(**parameters)
        obj.save()


class PurchaseListAPIView(generics.ListAPIView):
    """
    Контроллер списка закупок продуктов/товаров.
    """
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()
