from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.response import Response

from account.permissions import IsVeterinarianAccount
from .serializers import AddAppointmentSerializer, HospitalListSerializer, AppointmentResultSerializer, SearchAppointmentSerializer
from .models import Appointment, Hospital
from dog.models import Dog
from account.models import Account


class AddAppointmentViewSet(mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AddAppointmentSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            hospital = Hospital.objects.filter(id=serializer.data['hospital']).first()
            if not hospital:
                return Response({'Hospital is not exist'}, status=status.HTTP_400_BAD_REQUEST)

            dog = Dog.objects.filter(id=serializer.data['dog']).first()
            if not dog:
                return Response({'Dog is not exist'}, status=status.HTTP_400_BAD_REQUEST)

            if request.user.is_veterinarian:
                stat = False
            else:
                stat = True

            appointment = Appointment.objects.create(
                key=Appointment.generate_key(),
                hospital=hospital,
                dog=dog,
                date=serializer.data['date'],
                status=stat)
            appointment.save()
            return Response({'key': appointment.key}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HospitalViewSet(mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalListSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class SearchAppointmentViewSet(mixins.CreateModelMixin,
                         viewsets.GenericViewSet):
    queryset = Appointment.objects.all()
    serializer_class = SearchAppointmentSerializer
    permission_classes = (IsVeterinarianAccount,)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            from django.db.models import Q

            search = serializer.data['search']

            # appointment
            appointment = Appointment.objects.filter(key=search).first()
            if appointment:
                return Response({
                    'appointment_list': AppointmentResultSerializer(appointment).data,
                    'account': []
                }, status=status.HTTP_201_CREATED)

            appointment_list = []

            # dog
            dog_list = Dog.objects.filter(Q(name__icontains=search) | Q(location__icontains=search))
            if dog_list:
                for dog in dog_list:
                    appointment = Appointment.objects.filter(dog=dog).first()
                    if appointment:
                        appointment_list.append(appointment)

            # user
            account_list = Account.objects.filter(Q(first_name__icontains=search) | \
                                                  Q(last_name__icontains=search) | \
                                                  Q(tel_1__icontains=search) | \
                                                  Q(tel_2__icontains=search) | \
                                                  Q(address__icontains=search) | \
                                                  Q(email__icontains=search))
            if account_list:
                for account in account_list:
                    dog_list = Dog.objects.filter(account=account)
                    if dog_list:
                        for dog in dog_list:
                            appointment = Appointment.objects.filter(dog=dog).first()
                            if appointment and appointment not in appointment_list:
                                appointment_list.append(appointment)

            response = {
                'appointment_list': AppointmentResultSerializer(appointment_list, many=True).data,
                'account': []
            }

            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
