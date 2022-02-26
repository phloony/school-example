from django.urls import path, include
from rest_framework import routers
from .viewsets import (
    TeacherViewSet,
    ClassViewSet,
    SubjectViewSet
)


app_name = "classes"

router = routers.DefaultRouter()

router.register(r"teachers", TeacherViewSet)
router.register(r"classes", ClassViewSet)
router.register(r"subjects", SubjectViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
