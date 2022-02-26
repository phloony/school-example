from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory

from students.models import (Student,
                     Parent,
                     StudentClass,
                     StudentParent
                     )
from students.viewsets import (StudentViewSet,
                       ParentViewSet,
                       StudentClassViewSet,
                       StudentParentViewSet
                       )


class TestAPIs(TestCase):
    fixtures = ['initial_sample.json']

    def setUp(self):
        self.factory = APIRequestFactory()

    def test_studentslist_get(self):
        view = StudentViewSet.as_view({'get': 'list'})
        request = self.factory.get('/students/student/')
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_student_str(self):
        student = Student.objects.first()
        self.assertEqual(student.name, str(student))

    def test_parentslist_get(self):
        view = ParentViewSet.as_view({'get': 'list'})
        request = self.factory.get(reverse('students:parent-list'))
        response = view(request)
        self.assertEqual(response.status_code, 200)
    
    def test_parent_str(self):
        parent = Parent.objects.first()
        self.assertEqual(parent.name, str(parent))

    def test_studentclasslist_get(self):
        view = StudentClassViewSet.as_view({'get': 'list'})
        request = self.factory.get(reverse('students:studentclass-list'))
        response = view(request)
        self.assertEqual(response.status_code, 200)
    
    def test_studentclass_str(self):
        studentclass = StudentClass.objects.first()
        self.assertEqual(f"{studentclass.student} ({studentclass._class})", str(studentclass))

    def test_studentparentlist_get(self):
        view = StudentParentViewSet.as_view({'get': 'list'})
        request = self.factory.get(reverse('students:studentparent-list'))
        response = view(request)
        self.assertEqual(response.status_code, 200)
    
    def test_studentparent_str(self):
        studentparent = StudentParent.objects.first()
        self.assertEqual(f"{studentparent.student.name} - {studentparent.parent.name}", str(studentparent))
