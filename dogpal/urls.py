from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import DefaultRouter

from .views_home import *
from dog.views import *
from veterinarian.views import *
from vaccination.views import *
from account.views_register import *
from account.views_login import *
from finddog.views import *


schema_view = get_swagger_view(title='DogPal API')
router = DefaultRouter()

router.register(r'home', HomeViewSet)
router.register(r'add-dog', AddorEditDogViewSet)
router.register(r'delete-dog', DeleteDogViewSet)
router.register(r'add-image', AddDogImageViewSet)
router.register(r'add-appointment', AddAppointmentViewSet)
router.register(r'hospital', HospitalViewSet)
router.register(r'search-appointment', SearchAppointmentViewSet)
router.register(r'vaccine-book', VaccineBookViewSet)
router.register(r'dog', DogViewSet)
router.register(r'register', UserRegisterViewSet)
router.register(r'login', UserLoginViewSet)
router.register(r'finddog/add-image', AddImageViewSet)
router.register(r'finddog/distance', DistanceVectorViewSet)

urlpatterns = [
    url(r'^api/$', schema_view),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api/logout/', LogoutView.as_view()),
    url(r'^api/session/', CheckSessionExpired.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
