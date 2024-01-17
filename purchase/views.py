from rest_framework import generics

from purchase.models import Purchase
from purchase.serializers import PurchaseSerializer


class PurchaseCreateAPIView(generics.CreateAPIView):
    """
    Контроллер закупки продуктов/товаров.
    """
    model = Purchase
    serializer_class = PurchaseSerializer

    def perform_create(self, serializer):  # Увеличение иерархии +1. Иерархия максимум увеличивается до 3.
        obj = serializer.save()
        hierarchy = self.request.data.get('hierarchy')
        product_owner = self.request.data.get('product_owner')
        buyer = self.request.data.get('buyer')
        buyer = product_owner
        if obj.hierarchy <= 1:
            obj.hierarchy = hierarchy + 1
        else:
            obj.hierarchy = 2

        obj.save()


class PurchaseListAPIView(generics.ListAPIView):
    """
    Контроллер списка закупок продуктов/товаров.
    """
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()
