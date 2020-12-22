from rest_framework import routers
from .views import UserViewSet
from django.urls import path
from django.urls.conf import include

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls'), name='rest_framework')
]

