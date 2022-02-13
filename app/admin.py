from django.contrib import admin
from .models import Product, User, Category

# Register your models here.

admin.site.register(User)

@admin.register(Category)
class CatgeoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepoulated_fields ={'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'created', 'updated']
    list_editable = ['price']
    prepopulated_field = {'slug': ('name',)}

