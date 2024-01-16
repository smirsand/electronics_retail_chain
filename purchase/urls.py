from django.urls import path

from purchase.apps import PurchaseConfig
from purchase.views import PurchaseCreateAPIView, PurchaseListAPIView

app_name = PurchaseConfig.name

urlpatterns = [
    path('create', PurchaseCreateAPIView.as_view(), name='purchase_create'),
    path('list', PurchaseListAPIView.as_view(), name='purchase_list'),
]
