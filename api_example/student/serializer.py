from rest_framework import serializers
from .models import Student, CourseRegistration, Course

#class StudentSerializer(serializers.ModelSerializer):
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('url', 'id', 'Name', 'StudentId')

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('url', 'id', 'Description', 'Code','Professor','Capacity')

class CourseRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CourseRegistration
        fields = ('url', 'id', 'Name', 'CourseId')


# i think i'm missing something... but i'm going to roll with it
# and go from there.