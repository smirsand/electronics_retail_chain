from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from product.models import Product
from product.paginators import ProductPagination
from product.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ('name', 'quantity', 'city', 'country',)  # Набор полей для фильтрации
    pagination_class = ProductPagination
