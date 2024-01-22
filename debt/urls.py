from django.urls import path

from debt.apps import DebtConfig
from debt.views import DebtListAPIView, DebtRetrieveAPIView, DebtDestroyAPIView, DebtUpdateAPIView

app_name = DebtConfig.name

urlpatterns = [
    path('list/', DebtListAPIView.as_view(), name='debt-list'),
    path('retrieve/<int:pk>/', DebtRetrieveAPIView.as_view(), name='debt-retrieve'),
    path('update/<int:pk>/', DebtUpdateAPIView.as_view(), name='debt-update'),
    path('delete/<int:pk>/', DebtDestroyAPIView.as_view(), name='debt-destroy'),

]
