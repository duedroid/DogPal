from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from .views_home import HomeViewSet
from dog.views import DogDetailViewSet, AddDogImageViewSet, AddorEditDogViewSet
from veterinarian.views import AddAppointmentViewSet
from account.views_register import UserRegisterViewSet
from account.views_login import LogoutView, UserLoginViewSet


schema_view = get_swagger_view(title='DogPal API')
router = DefaultRouter()

router.register(r'home', HomeViewSet)
router.register(r'add-dog', AddorEditDogViewSet)
router.register(r'add-image', AddDogImageViewSet)
router.register(r'add-appointment', AddAppointmentViewSet)
router.register(r'dog', DogDetailViewSet)
router.register(r'register', UserRegisterViewSet)
router.register(r'login', UserLoginViewSet)

urlpatterns = [
    url(r'^api/$', schema_view),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api/logout/', LogoutView.as_view()),
    # url(r'^api/login/', obtain_jwt_token),
    url(r'^api/token-refresh/', refresh_jwt_token),
    url(r'^api/token-verify/', verify_jwt_token),
]
