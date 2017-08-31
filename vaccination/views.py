from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.response import Response

from account.permissions import IsVeterinarianAccount
from .serializers import RecieveAppointmentSerializer, VaccineForBookSerializer, VaccineRecordBookSerailizer
from .models import *
from veterinarian.models import Appointment
from account.models import Account


class VaccineBookViewSet(mixins.CreateModelMixin,
                         viewsets.GenericViewSet):
    queryset = VaccineFor.objects.all()
    serializer_class = RecieveAppointmentSerializer
    permission_classes = (IsVeterinarianAccount,)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            appointment = Appointment.objects.filter(key=serializer.data['appointment_key']).first()
            if not appointment:
                return Response({'Appointment is not exist'}, status=status.HTTP_400_BAD_REQUEST)

            vaccinefor = VaccineFor.objects.filter(appointment=appointment)
            vaccinerecord = VaccineRecord.objects.filter(dog=appointment.dog)
            context = {'hospital': appointment.hospital}
            response = {
                'vaccine_for': VaccineForBookSerializer(vaccinefor, context=context, many=True).data,
                'vaccine_record': VaccineRecordBookSerailizer(vaccinerecord, many=True).data,
                'dog': appointment.dog.id,
                'account': appointment.dog.account.id
            }

            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
