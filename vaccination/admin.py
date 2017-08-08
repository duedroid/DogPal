from django.contrib import admin
from .models import VaccineFor, VaccineRecord, VaccineStockDetail


@admin.register(VaccineFor)
class VaccineForAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(VaccineRecord)
class VaccineRecordAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(VaccineStockDetail)
class VaccineStockDetailAdmin(admin.ModelAdmin):
    list_display = ('brand',)
    search_fields = ('brand',)
