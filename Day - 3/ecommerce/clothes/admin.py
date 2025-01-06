from django.contrib import admin
from .models import Clothes
# Register your models here.

@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'stock', 'available')

