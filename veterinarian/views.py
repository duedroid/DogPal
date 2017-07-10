from rest_framework import viewsets, mixins

from .serializers import AddAppointmentSerializer
from .models import Appointment

class AddAppointmentViewSet(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AddAppointmentSerializer
