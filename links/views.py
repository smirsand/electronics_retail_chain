from rest_framework import viewsets

from links.models import Link
from links.serializers import LinkSerializer


class LinkViewSet(viewsets.ModelViewSet):
    """
    Контроллер модели Link.
    """
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
