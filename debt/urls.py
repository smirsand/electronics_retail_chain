from django.urls import path

from debt.apps import DebtConfig
from debt.views import DebtListAPIView

app_name = DebtConfig.name

urlpatterns = [
    path('debts/list/', DebtListAPIView.as_view(), name='debt_list'),
]
