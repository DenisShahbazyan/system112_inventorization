from items.models import Items
from .serializers import ItemSerializer
from rest_framework import viewsets


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer
