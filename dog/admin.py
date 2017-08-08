from django.contrib import admin
from .models import Dog, Picture

@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('id',)
