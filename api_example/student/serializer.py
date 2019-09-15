from rest_framework import serializers
from .models import Student, Course
#Surplus line, view the comments in 'models.py' for more info
#from .models import CourseRegistration

# testing out the HyperlinkedMode version, which i liked more!
#class StudentSerializer(serializers.ModelSerializer):
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('url', 'id', 'Name', 'StudentId', 'Courses')

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('url', 'id', 'Description', 'Code','Professor','Capacity')

#Surplus line, view the comments in 'models.py' for more info
#class CourseRegistrationSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = CourseRegistration
#        fields = ('url', 'id', 'Name', 'CourseId')
