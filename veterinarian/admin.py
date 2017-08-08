from django.contrib import admin
from .models import VetHos, Hospital, Appointment


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(VetHos)
class VetHosAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('date',)
