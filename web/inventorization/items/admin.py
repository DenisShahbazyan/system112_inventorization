from django.contrib import admin

from .models import Address, Items


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'address')
    list_editable = ('address',)
    list_filter = ('address',)


@admin.register(Items)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'inventory_number', 'location', 'room',
                    'clear_name', 'brand_or_model', 'serial_number', 'owner',
                    'remark')
    list_editable = ('inventory_number', 'location', 'room', 'clear_name',
                     'brand_or_model', 'serial_number', 'owner', 'remark')
    search_fields = ('username', 'email', 'is_staff')
    list_filter = ('inventory_number', 'location', 'room', 'clear_name',
                   'brand_or_model', 'serial_number', 'owner', 'remark')
