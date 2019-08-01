from django.contrib import admin
from django import forms

from .models import *


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('__all__')


class ItemInline(admin.StackedInline):
    form  = ItemForm
    model = Item
    # readonly_fields = ('token', 'create_date', 'sent_date',
                       # 'sent', 'identity', 'used')
    # fieldsets = (
                    # (None, { 'fields' :
                               # (('identity', 'is_active'),
                                # ('token', ),
                                # ('sent', 'sent_date'),
                                # ('valid_until',),
                                # ('used',),
                                # ('create_date',))
                           # }
                    # ),
                # )
    extra = 0


@admin.register(Item)
class Item(admin.ModelAdmin):
    list_display = ('name',
                    'ordering',
                    'is_active')
    list_filter = ('name', 'is_active',)
    list_editable = ('is_active','ordering')
    search_fields = ('name',)
    exclude = ('slug',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'ordering',
                    'is_active')
    list_filter = ('name', 'is_active',)
    list_editable = ('is_active','ordering')
    search_fields = ('name',)
    exclude = ('slug',)
    inlines = [ItemInline,]
