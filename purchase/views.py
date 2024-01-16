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
        if obj.hierarchy <= 2:
            obj.hierarchy = hierarchy + 1
        else:
            obj.hierarchy = 3

        obj.save()


class PurchaseListAPIView(generics.ListAPIView):
    """
    Контроллер списка закупок продуктов/товаров.
    """
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()
