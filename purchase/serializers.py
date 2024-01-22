from rest_framework import serializers

from purchase.models import Purchase


class PurchaseSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели Purchase.
    """

    class Meta:
        model = Purchase
        fields = '__all__'
