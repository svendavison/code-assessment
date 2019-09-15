from django.shortcuts import render
from rest_framework import viewsets

from .models import Student
from .serializer import StudentSerializer

# uses the standards from django for CRUD
class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
