from rest_framework import serializers

from utils.serializers import Base64ImageField
from .models import Image


class UploadImageSerializer(serializers.ModelSerializer):
    image = Base64ImageField(max_length=None, use_url=False, allow_empty_file=False, allow_null=False, required=True)

    class Meta:
        model = Image
        fields = ('name', 'image')


class DistanceVectorSerializer(serializers.Serializer):
    name_1 = serializers.CharField(max_length=255, required=True)
    name_2 = serializers.CharField(max_length=255, required=True)
