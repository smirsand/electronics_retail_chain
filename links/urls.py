from links.apps import LinksConfig
from rest_framework.routers import DefaultRouter

from links.views import LinkViewSet

app_name = LinksConfig.name

router = DefaultRouter()
router.register(r'link', LinkViewSet, basename='link')

urlpatterns = [

              ] + router.urls