from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import DefaultRouter

from .views_home import HomeViewSet
from doginformation.views import AddDogViewSet, DogDetailViewSet
from veterinarian.views import AddAppointmentViewSet
from userinformation.views import UserRegisterViewSet

schema_view = get_swagger_view(title='Pastebin API')
router = DefaultRouter()

router.register(r'home', HomeViewSet)
router.register(r'add-dog', AddDogViewSet)
router.register(r'add-appointment', AddAppointmentViewSet)
router.register(r'dog', DogDetailViewSet)
router.register(r'register', UserRegisterViewSet)

urlpatterns = [
    url(r'^docs/$', schema_view),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),

    # url(r'^signup/$', SignUpView),
]
