from django.contrib import admin

from .models import Vetarinarian, VetHos, Hospital, Appointment


admin.site.register(Vetarinarian)
admin.site.register(VetHos)
admin.site.register(Hospital)
admin.site.register(Appointment)
