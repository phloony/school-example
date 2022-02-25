from rest_framework import serializers
from .models import (Teacher,
                     Subject,
                     Class,
                     )


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['name', 'cpf', 'rg', 'phone_number', 'address', 'subjects']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['name']


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['teacher', 'subject']
