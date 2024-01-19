from rest_framework import generics

from debt.models import Debt
from debt.serializers import DebtSerializer


class DebtListAPIView(generics.ListAPIView):
    """
    Контроллер списка задолженности.
    """

    serializer_class = DebtSerializer
    queryset = Debt.objects.all()


class DebtRetrieveAPIView(generics.RetrieveAPIView):
    """
    Контроллер просмотра задолженности.
    """

    serializer_class = DebtSerializer
    queryset = Debt.objects.all()


class DebtDestroyAPIView(generics.DestroyAPIView):
    """
    Контроллер удаления задолженности.
    """

    queryset = Debt.objects.all()
