from rest_framework import viewsets

from links.models import Link
from links.serliazers import LinkSerializer


class LinkViewSet(viewsets.ModelViewSet):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
