from django.contrib import admin
from .models import Blog
# Register your models here.
@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author')
