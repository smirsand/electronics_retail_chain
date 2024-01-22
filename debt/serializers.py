from rest_framework import serializers

from debt.models import Debt


class DebtSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели Debt.
    """

    class Meta:
        model = Debt
        fields = '__all__'
