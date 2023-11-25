from django.contrib import admin
from .models import Category, Product
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    # parler doesn’t support the prepopulated_fields attribute, but it does support the get_prepopulated_fields()
    prepopulated_fields = {'slug': ('name',)}

    # def get_prepopulated_fields(self, request, obj=None):
    #     return {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    # def get_prepopulated_fields(self, request, obj=None):
    #     return {'slug': ('name',)}
