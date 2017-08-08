from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import DefaultRouter

from .views_home import HomeViewSet
from dog.views import AddDogViewSet, DogDetailViewSet
from veterinarian.views import AddAppointmentViewSet
from account.views_register import UserRegisterViewSet
from account.views_login import UserLoginViewSet, LogoutView


schema_view = get_swagger_view(title='Pastebin API')
router = DefaultRouter()

router.register(r'home', HomeViewSet)
router.register(r'add-dog', AddDogViewSet)
router.register(r'add-appointment', AddAppointmentViewSet)
router.register(r'dog', DogDetailViewSet)
router.register(r'register', UserRegisterViewSet)
router.register(r'login', UserLoginViewSet)

urlpatterns = [
    url(r'^docs/$', schema_view),
    url(r'^admin/', admin.site.urls),
    url(r'^api/logout/$', LogoutView.as_view()),
    url(r'^api/', include(router.urls)),
]
