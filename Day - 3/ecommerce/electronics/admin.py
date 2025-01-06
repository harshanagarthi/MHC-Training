from django.contrib import admin
from .models import Electronics
# Register your models here.
@admin.register(Electronics)
class ElectronicsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'stock', 'available')