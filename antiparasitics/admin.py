from django.contrib import admin
from .models import AntiParasitics, Therapy


@admin.register(AntiParasitics)
class AntiParasiticsAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(Therapy)
class TherapyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
