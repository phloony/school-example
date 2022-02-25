from rest_framework.viewsets import ModelViewSet

from .models import (
    Teacher,
    Subject,
    Class
)
from .serializers import (
    TeacherSerializer,
    SubjectSerializer,
    ClassSerializer
)


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    filterset_fields = ('id', 'name', 'rg', 'cpf')


class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    filterset_fields = ('id', 'name')


class ClassViewSet(ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

