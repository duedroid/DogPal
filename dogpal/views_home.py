from rest_framework import viewsets, mixins
from .serializers import HomeSerializer
from account.models import Account
from dog.models import Dog
from rest_framework.response import Response


class HomeViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Account.objects.all()
    serializer_class = HomeSerializer

    def list(self, request):
        queryset = Account.objects.filter(account=request.user).first()
        serializer = HomeSerializer(queryset, many=True)
        return Response(serializer.data)
