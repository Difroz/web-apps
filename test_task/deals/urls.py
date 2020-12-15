from django.urls import re_path, include
from rest_framework import routers
from .views import UploadViewSet

router = routers.DefaultRouter()
router.register(r'upload', UploadViewSet, basename="upload")

urlpatterns = [
    re_path(r'^', include(router.urls)),
]
