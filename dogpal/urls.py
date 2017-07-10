from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import DefaultRouter

from doginformation.views import HomeViewSet

schema_view = get_swagger_view(title='Pastebin API')
router = DefaultRouter()

router.register(r'home', HomeViewSet)

urlpatterns = [
    url(r'^docs/$', schema_view),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),

    # url(r'^signup/$', SignUpView),

    # url(r'^rest-auth/', include('rest_auth.urls')),
    # url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
]
