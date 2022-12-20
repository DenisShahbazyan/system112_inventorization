from rest_framework import serializers

from items.models import Items


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = (
            'id', 'user', 'inventory_number', 'address', 'location', 'room',
            'clear_name', 'brand_or_model', 'serial_number', 'owner', 'image',
            'remark'
        )
