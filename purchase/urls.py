from django.urls import path

from purchase.apps import PurchaseConfig
from purchase.views import PurchaseCreateAPIView, PurchaseListAPIView, PurchaseRetrieveAPIView, PurchaseDestroyAPIView

app_name = PurchaseConfig.name

urlpatterns = [
    path('create', PurchaseCreateAPIView.as_view(), name='purchase-create'),
    path('list', PurchaseListAPIView.as_view(), name='purchase-list'),
    path('retrieve/<int:pk>/', PurchaseRetrieveAPIView.as_view(), name='purchase-retrieve'),
    path('delete/<int:pk>/', PurchaseDestroyAPIView.as_view(), name='purchase-destroy'),
]
