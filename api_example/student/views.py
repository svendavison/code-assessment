from django.shortcuts import render
from rest_framework import viewsets

from .models import Student, CourseRegistration, Course
from .serializer import StudentSerializer, CourseRegistrationSerializer, CourseSerializer

# uses the standards from django for CRUD
class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseRegistrationView(viewsets.ModelViewSet):
    queryset = CourseRegistration.objects.all()
    serializer_class = CourseRegistrationSerializer

