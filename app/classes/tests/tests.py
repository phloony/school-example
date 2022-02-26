from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory

from classes.models import (Teacher,
                     Subject,
                     Class
                     )
from classes.viewsets import (TeacherViewSet,
                       SubjectViewSet,
                       ClassViewSet
                       )


class TestAPIs(TestCase):
    fixtures = ['initial_sample.json']

    def setUp(self):
        self.factory = APIRequestFactory()

    def test_teacherslist_get(self):
        view = TeacherViewSet.as_view({'get': 'list'})
        request = self.factory.get(reverse('classes:teacher-list'))
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_teacher_str(self):
        teacher = Teacher.objects.first()
        self.assertEqual(teacher.name, str(teacher))

    def test_subjectslist_get(self):
        view = SubjectViewSet.as_view({'get': 'list'})
        request = self.factory.get(reverse('classes:subject-list'))
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_subject_str(self):
        subject = Subject.objects.first()
        self.assertEqual(subject.name, str(subject))

    def test_classeslist_get(self):
        view = ClassViewSet.as_view({'get': 'list'})
        request = self.factory.get(reverse('classes:class-list'))
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_class_str(self):
        cl = Class.objects.first()
        self.assertEqual(f"{cl.teacher.name} - {cl.subject.name}", str(cl))
