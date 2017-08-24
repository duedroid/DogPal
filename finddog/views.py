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
        if serializer.is_valid() and serializer.data['name_1'] != serializer.data['name_2']:
            image_1 = Image.objects.filter(name=serializer.data['name_1']).first()
            image_2 = Image.objects.filter(name=serializer.data['name_2']).first()

            if not image_1 or not image_2:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            url = 'http://161.246.6.240:10100/server/dog/extract_features/'

            import requests
            import json
            if not image_1.vector:
                file = {'path': open(image_1.image.path, 'rb').read()}
                r = json.loads(requests.post(url, files=file).content.decode('utf-8'))
                image_1.vector = r['payload']['reduced_features']
                image_1.save(update_fields=['vector'])
            if not image_2.vector:
                file = {'path': open(image_2.image.path, 'rb').read()}
                r = json.loads(requests.post(url, files=file).content.decode('utf-8'))
                image_2.vector = r['payload']['reduced_features']
                image_2.save(update_fields=['vector'])

            import ast
            from math import sqrt
            from numpy import linalg as LA
            vector_1 = json.loads(image_1.vector) if type(image_1.vector) == str else image_1.vector
            vector_2 = json.loads(image_2.vector) if type(image_2.vector) == str else image_2.vector

            norm_vector_1 = LA.norm(vector_1)
            norm_vector_2 = LA.norm(vector_2)
            for i in range(0,14):
                vector_1[i] /= norm_vector_1
                vector_2[i] /= norm_vector_2

            distance_power_of_2 = 0
            for i in range(0,14):
                distance_power_of_2 += (vector_1[i]-vector_2[i])**2
            distance = sqrt(distance_power_of_2)

            return Response({'distance': distance})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
