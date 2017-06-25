from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from userinformation.views import ProfileViewSet


schema_view = get_swagger_view(title='Pastebin API')

router = routers.SimpleRouter()
router.register(r'login', ProfileViewSet)

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls))
]
