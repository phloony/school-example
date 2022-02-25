from rest_framework import serializers
from .models import (Parent,
                     Student,
                     StudentClass,
                     StudentParent)


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ['name', 'cpf', 'rg', 'phone_number', 'address']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'rg', 'parents', 'grade', 'classes']


class StudentClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentClass
        fields = ['student', '_class']


class StudentParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentParent
        fields = ['student', 'parent']
