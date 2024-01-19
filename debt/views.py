from rest_framework import generics

from debt.models import Debt
from debt.serializers import DebtSerializer


class DebtListAPIView(generics.ListAPIView):
    """
    Контроллер списка задолженности.
    """

    serializer_class = DebtSerializer
    queryset = Debt.objects.all()
