from django.urls import include, path
from rest_framework import routers

from .views import ItemViewSet

app_name = 'api'

router = routers.DefaultRouter()

router.register('items', ItemViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
