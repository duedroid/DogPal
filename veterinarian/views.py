from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import AddAppointmentSerializer, HospitalListSerializer
from dog.serializers import DogNameListSerializer
from .models import Appointment, Hospital
from dog.models import Dog


class AddAppointmentViewSet(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AddAppointmentSerializer
    permissions_classes = (IsAuthenticated,)

    def list(self, request):
        if request.user.is_veterinarian:
            return Response(status=status.HTTP_403_FORBIDDEN)

        dog = Dog.objects.filter(account=request.user)
        hospital = Hospital.objects.all()
        serializer = DogNameListSerializer(dog, many=True).data
        serializer.append({
            'hospital': HospitalListSerializer(hospital, many=True).data
        })
        return Response(serializer)

    def create(self, request):
        if request.user.is_veterinarian:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            appointment = Appointment.objects.create(
                hospital=serializer.data['hospital'],
                dog=serializer.data['dog'],
                date=serializer.data['date'],
                status=serializer.data['status'])
            appointment.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
