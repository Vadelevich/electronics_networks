from django.contrib import admin

from electronics.models import Supplier, Product, Contact


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'contact', 'product', 'parent', 'debt', ]
    list_display_links = ['parent']
    list_filter = ['contact__city']
    actions = ['make_clean']

    @admin.action(description='Очистить задолженность перед поставщиком у выбранных объектов')
    def make_clean(self, request, queryset):
        queryset.update(debt=None)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'model', 'date', ]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'country', 'city', 'street', 'house_number']
