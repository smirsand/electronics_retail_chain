from rest_framework import serializers

from debt.models import Debt


class DebtSerializer(serializers.ModelSerializer):

    class Meta:
        model = Debt
        fields = '__all__'
        read_only_fields = ['debt']
