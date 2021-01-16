from django.contrib import admin

# Register your models here.
from .models import NewTable, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'qty')

admin.site.register(NewTable)
admin.site.register(Product, ProductAdmin)
