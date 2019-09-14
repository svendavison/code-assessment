from django import forms
from .models import Courses
from .models import Students

class CoursesForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['Description','Code','Professor','Capacity']

        
class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['Name', 'StudentId']
