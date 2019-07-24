from django.contrib import admin

from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'ordering',
                    'is_active')
    list_filter = ('name', 'is_active',)
    list_editable = ('is_active','ordering')
    search_fields = ('name',)
    exclude = ('slug',)


@admin.register(Item)
class Item(admin.ModelAdmin):
    list_display = ('name',
                    'ordering',
                    'is_active')
    list_filter = ('name', 'is_active',)
    list_editable = ('is_active','ordering')
    search_fields = ('name',)
    exclude = ('slug',)
