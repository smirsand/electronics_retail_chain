from rest_framework.routers import DefaultRouter

from links.apps import LinksConfig
from links.views import LinkViewSet

app_name = LinksConfig.name

router = DefaultRouter()  # маршрутизатор по умолчанию
router.register(r'link', LinkViewSet, basename='link')

urlpatterns = [] + router.urls
