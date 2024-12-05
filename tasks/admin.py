from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    
admin.register(Item, ItemAdmin)
# Register your models here.
