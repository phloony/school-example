from rest_framework.viewsets import ModelViewSet

from .models import (
    Parent,
    Student,
    StudentClass,
    StudentParent
)
from .serializers import (
    ParentSerializer,
    StudentSerializer,
    StudentClassSerializer,
    StudentParentSerializer
)


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filterset_fields = ('id', 'name', 'rg')
    http_method_names = ['get', 'post', 'put', 'delete']


class ParentViewSet(ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    filterset_fields = ('id', 'name', 'cpf', 'rg')
    http_method_names = ['get', 'post', 'put', 'delete']


class StudentClassViewSet(ModelViewSet):
    queryset = StudentClass.objects.all()
    serializer_class = StudentClassSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class StudentParentViewSet(ModelViewSet):
    queryset = StudentParent.objects.all()
    serializer_class = StudentParentSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
