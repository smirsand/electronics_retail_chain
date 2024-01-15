from django.urls import path

from product.apps import ProductConfig
from product.views import ProductListView

app_name = ProductConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
]
