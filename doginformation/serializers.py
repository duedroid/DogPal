from rest_framework import serializers

from userinformation.models import Profile
from .models import Dog, DogPicture
from veterinarian.models import Appointment, Hospital
from dogpal.serializers import DogPictureSerializer


class AddDogSerializer(serializers.ModelSerializer):
    dogpicture = DogPictureSerializer(many=True)

    class Meta:
        model = Dog
        fields = ('dogpicture', 'profile', 'name', 'blood_type', 'breed', 'current_weight', 'age', 'birth_day', 'is_sterize', 'gender', 'micro_no', 'color_primary', 'color_secondary', 'location', 'dominance', 'status')


    # def create(self, request, *args, **kwargs):
    #     data=request.DATA

    #     f = Foo.objects.create()

    #     # ... create nested objects from request data ...

    #     # ...
    #     return Response(serializer.data,
    #                     status=status.HTTP_201_CREATED,
    #                     headers=headers)
