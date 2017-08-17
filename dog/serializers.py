from rest_framework import serializers

from account.models import Account
from .models import Dog, Picture
from veterinarian.models import Appointment, Hospital
from vaccination.models import VaccineRecord
from vaccination.serializers import VaccineRecordSerailizer


class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr
        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension
        if extension is None:
            extension = 'jpg'
        return extension


class DogImageSerializer(serializers.ModelSerializer):
    image = Base64ImageField(max_length=None, use_url=True, allow_empty_file=True, allow_null=True, required=False)

    class Meta:
        model = Picture
        fields = ('id', 'image')


class AddorEditDogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = ('name', 'blood_type', 'breed', 'current_weight',
                  'age', 'birth_day', 'is_sterize', 'gender',
                  'micro_no', 'color_primary', 'color_secondary',
                  'location', 'dominance', 'status')


class DogDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = ('name', 'blood_type', 'breed', 'current_weight',
                  'age', 'birth_day', 'is_sterize', 'gender',
                  'micro_no', 'color_primary', 'color_secondary',
                  'location', 'dominance')

    def to_representation(self, instance):
        data = super(DogDetailSerializer, self).to_representation(instance)
        data.update({
            'vaccination': VaccineRecordSerailizer(VaccineRecord.objects.filter(dog=instance.id), many=True).data,
            'dogpicture': DogPictureSerializer(Picture.objects.filter(dog=instance.id), many=True).data
        })
        return data
