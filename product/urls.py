from rest_framework.routers import DefaultRouter

from product.apps import ProductConfig
from product.views import ProductViewSet

app_name = ProductConfig.name

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [] + router.urls
