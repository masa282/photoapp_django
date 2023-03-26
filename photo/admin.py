from django.contrib import admin
from .models import Category, PhotoPost

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    list_display_links = ["id", "title"]


class PhotoPostAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    list_display_links = ["id", "title"]

    
admin.site.register(Category)
admin.site.register(PhotoPost)
