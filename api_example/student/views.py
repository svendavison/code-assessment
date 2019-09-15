from django.shortcuts import render
from rest_framework import viewsets

from .models import Student, Course
#Surplus line, view the comments in 'models.py' for more info
#from .models import CourseRegistration
from .serializer import StudentSerializer, CourseSerializer
#Surplus line, view the comments in 'models.py' for more info
#from .serializer import CourseRegistrationSerializer

# uses the standards from django for CRUD
class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

#Surplus line, view the comments in 'models.py' for more info
#class CourseRegistrationView(viewsets.ModelViewSet):
#    queryset = CourseRegistration.objects.all()
#    serializer_class = CourseRegistrationSerializer

