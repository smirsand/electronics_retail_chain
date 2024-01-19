from rest_framework import generics

from debt.models import Debt
from debt.permissions import IsNotSuperuser
from debt.serializers import DebtSerializer


class DebtListAPIView(generics.ListAPIView):
    """
    Контроллер списка задолженности.
    """

    serializer_class = DebtSerializer
    queryset = Debt.objects.all()

    # def get_queryset(self):
    #     # получаем базовый набор объектов из родительского класса.
    #     queryset = super().get_queryset()
    #     print(queryset)
    #     # фильтруем объекты, оставляя те, которые принадлежат текущему пользователю.
    #     # queryset = queryset.filter(user=self.request.user)
    #     return queryset


class DebtRetrieveAPIView(generics.RetrieveAPIView):
    """
    Контроллер просмотра задолженности.
    """

    serializer_class = DebtSerializer
    queryset = Debt.objects.all()


class DebtUpdateAPIView(generics.UpdateAPIView):
    """
    Контроллер редактирования задолженности.
    """
    serializer_class = DebtSerializer
    queryset = Debt.objects.all()
    permission_classes = [IsNotSuperuser]


class DebtDestroyAPIView(generics.DestroyAPIView):
    """
    Контроллер удаления задолженности.
    """

    queryset = Debt.objects.all()
    permission_classes = [IsNotSuperuser]
