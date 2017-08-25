from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import DefaultRouter

from .views_home import HomeViewSet
from dog.views import DogViewSet, AddDogImageViewSet, AddorEditDogViewSet
from veterinarian.views import AddAppointmentViewSet
from account.views_register import UserRegisterViewSet
from account.views_login import LogoutView, UserLoginViewSet
from finddog.views import AddImageViewSet, DistanceVectorViewSet


schema_view = get_swagger_view(title='DogPal API')
router = DefaultRouter()

router.register(r'home', HomeViewSet)
router.register(r'add-dog', AddorEditDogViewSet)
router.register(r'add-image', AddDogImageViewSet)
router.register(r'add-appointment', AddAppointmentViewSet)
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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
