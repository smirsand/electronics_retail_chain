from django.urls import path

from debt.apps import DebtConfig
from debt.views import DebtListAPIView, DebtRetrieveAPIView, DebtDestroyAPIView

app_name = DebtConfig.name

urlpatterns = [
    path('debts/list/', DebtListAPIView.as_view(), name='debt-list'),
    path('debts/<int:pk>/', DebtRetrieveAPIView.as_view(), name='debt-retrieve'),
    path('debts/delete/<int:pk>/', DebtDestroyAPIView.as_view(), name='debt-destroy'),

]
