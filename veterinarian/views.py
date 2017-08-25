from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import AddAppointmentSerializer
from .models import Appointment, Hospital
from dog.models import Dog


class AddAppointmentViewSet(mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AddAppointmentSerializer

    def create(self, request):
        if request.user.is_veterinarian:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            hospital = Hospital.objects.filter(id=serializer.data['hospital']).first()
            if not hospital:
                return Response({'Hospital is not exist'}, status=status.HTTP_400_BAD_REQUEST)

            dog = Dog.objects.filter(id=serializer.data['dog']).first()
            if not dog:
                return Response({'Dog is not exist'}, status=status.HTTP_400_BAD_REQUEST)

            appointment = Appointment.objects.create(
                hospital=hospital,
                dog=dog,
                date=serializer.data['date'],
                status=True)
            appointment.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
