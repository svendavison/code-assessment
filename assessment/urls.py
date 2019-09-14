from django.urls import path
#from .views import list_products, create_product, update,product, delete_product
from .views import list_courses, update_course, add_course, delete_course
from .views import list_students, add_student, delete_student, update_student

urlpatterns = [
    #path('', list_products, name='list_products'),
    #path('new', create_product, name='create_products'),
    #path('update/<int:id>/', update_product, name='update_product'),
    #path('delete/<int:id>/', delete_product, name='delete_product'),

    path('', list_courses, name='list_courses'),

    path('course/all', list_courses, name='list_courses'),
    path('course/update/<int:id>', update_course, name='update_course'),    
    path('course/delete/<int:id>', delete_course, name='delete_course'),
    path('course/add', add_course, name='add_course'),

    path('student/all', list_students, name='list_students'),
    path('student/update/<int:id>', update_student, name='update_student'),
    path('student/delete/<int:id>', delete_student, name='delete_student'),
    path('student/add', add_student, name='add_student'),

]

#CRUD* Courses w/
#Description
#Code
#Professor
#Capacity

#CRUD Students w/
#Name
#Student Id

############## REST ENDPOINTS ###########
# ReST end points w/
# Assign student to course
# ../student/enroll/<course id>
# Remove a student from a course
# ../student/drop/<course id> 
# Fetch all students in a course
# ../course/students
# Fetch students
# ../student/all
# Fetch all courses
# ../course/all