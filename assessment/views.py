from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Courses
from .models import Students
from .forms import CoursesForm
from .forms import StudentsForm

###########
# COURSES #
###########
#response = "math is your class " + str(id)
#return HttpResponse(response)
def list_courses(request):
    courseList = Courses.objects.all()
    return render(request, 'courses.html', {'courses': courseList})

def update_course(request, id):
    #response = "bobs your uncle " + str(id)
    #return HttpResponse(response)
    course = Courses.objects.get(Code=id)
    form = CoursesForm(request.POST or None, instance=course)
    if form.is_valid():
        form.save()
        return redirect('list_courses')
    return render(request, 'Courses-form.html', {'form': form})

def add_course(request):
    form = CoursesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_courses')
    return render(request, 'Courses-form.html', {'form': form})
    
# needs some work but it'll do for now. form isn't seeing 'course' atm.
def delete_course(request, id):
    course = Courses.objects.get(Code=id)
    if request.method == 'POST':
        course.delete()
        return redirect('list_courses')
    return render(request, 'course-delete-confirm.html', {'courses': course})

############
# STUDENTS #
############
#response = "bobs your uncle " + str(id)
#return HttpResponse(response)
def list_students(request):
    studentList = Students.objects.all()
    return render(request, 'students.html', {'students': studentList})

def add_student(request):
    form = StudentsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_students')
    return render(request, 'Student-form.html', {'form': form})

# needs some work but it'll do for now. form isn't seeing 'student' atm.
def delete_student(request, id):
    student = Students.objects.get(StudentId=id)
    if request.method == 'POST':
        student.delete()
        return redirect('list_students')
    return render(request, 'student-delete-confirm.html', {'students': student})

def update_student(request, id):
    student = Students.objects.get(StudentId=id)
    form = StudentsForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('list_students')
    return render(request, 'Student-form.html', {'form': form})

