from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from django.conf import settings


from .serializers import UploadImageSerializer, DistanceVectorSerializer
from .models import Image


class AddImageViewSet(mixins.CreateModelMixin,
                      viewsets.GenericViewSet):
    queryset = Image.objects.all()
    serializer_class = UploadImageSerializer
    permission_classes = (AllowAny,)
    parser_classes = (FormParser, MultiPartParser)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        has_image = Image.objects.filter(name=request.data['name']).first()
        if serializer.is_valid() and not has_image:
            image = Image.objects.create(name=serializer.data['name'],
                                         image=request.data.get('image'))
            image.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DistanceVectorViewSet(mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    queryset = Image.objects.all()
    serializer_class = DistanceVectorSerializer
    permission_classes = (AllowAny,)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            image_1 = Image.objects.filter(name=serializer.data['name_1']).first()
            image_2 = Image.objects.filter(name=serializer.data['name_2']).first()

            if not image_1 or not image_2:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            url = 'http://161.246.6.240:10100/server/dog/extract_features/'

            import requests
            import json
            if not image_1.vector:
                file = {'path': open(settings.BASE_DIR+image_1.image.url, 'rb').read()}
                r = json.load(requests.post(url, files=file).content)
                image_1.vector = r['payload']['reduced_features']
                image_1.save(update_fields=['vector'])
            if not image_2.vector:
                file = {'path': open(settings.BASE_DIR+image_2.image.url, 'rb').read()}
                r = json.load(requests.post(url, files=file).content)
                image_2.vector = r['payload']['reduced_features']
                image_2.save(update_fields=['vector'])

            import ast
            from math import sqrt
            vector_1 = ast.literal_eval(image_1.vector)
            vector_2 = ast.literal_eval(image_2.vector)
            distance_power_of_2 = 0
            for i in range(0,14):
                distance_power_of_2 += (vector_1[i]-vector_2[i])**2
            distance = sqrt(distance_power_of_2)

            return Response({'distance': distance})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
