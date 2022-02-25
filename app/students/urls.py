from django.urls import path, include
from rest_framework import routers
from .viewsets import (
    ParentViewSet,
    StudentViewSet,
    StudentClassViewSet,
    StudentParentViewSet
)


app_name = "students"

router = routers.DefaultRouter()

router.register(r"parents", ParentViewSet)
router.register(r"students", StudentViewSet)
router.register(r"student_classes", StudentClassViewSet)
router.register(r"student_parents", StudentParentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
