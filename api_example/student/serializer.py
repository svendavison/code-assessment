from rest_framework import serializers
from .models import Student

#class StudentSerializer(serializers.ModelSerializer):
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('url', 'id', 'name', 'studentId')