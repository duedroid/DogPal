from django.contrib import admin

from .models import VetHos, Hospital, Appointment


admin.site.register(VetHos)
admin.site.register(Hospital)
admin.site.register(Appointment)
