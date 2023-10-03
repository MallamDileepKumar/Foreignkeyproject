from django.contrib import admin
from .models import Category,Product

# Edit the Admin pages
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','Category','created_date')
    list_display_links = ('product_name',)
    list_filter = ('Category','created_date')
    list_editable = ('Category',)
    list_per_page = 1
    readonly_fields = ('Category',)

# Register your models here.
admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
