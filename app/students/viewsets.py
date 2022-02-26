from rest_framework.viewsets import ModelViewSet

from .models import (
    Parent,
    Student,
    StudentClass,
    StudentParent
)
from classes.models import Teacher, Class
from .serializers import (
    ParentSerializer,
    StudentSerializer,
    StudentClassSerializer,
    StudentParentSerializer
)
from django_filters import rest_framework as filters
import django_filters


class StudentFilter(django_filters.FilterSet):
    teachers = filters.ModelMultipleChoiceFilter(
        field_name='classes__teacher__name',
        to_field_name='name',
        queryset=Teacher.objects.all()
    )
    classes = filters.ModelMultipleChoiceFilter(
        queryset=Class.objects.all()
    )
    class Meta:
        model = Student
        fields = ['id', 'name', 'rg', 'teachers', 'classes']


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filterset_class = StudentFilter
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
