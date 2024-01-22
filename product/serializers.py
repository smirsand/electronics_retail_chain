from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели Product.
    """

    class Meta:
        model = Product
        fields = '__all__'
