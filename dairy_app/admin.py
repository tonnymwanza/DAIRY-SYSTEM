from django.contrib import admin

from . models import Products
from . models import Contact
# Register your models here.

@admin.register(Products)
class AdminProducts(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'image'
    ]

@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'subject',
        'message'
    ]