from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

from student.models import Course, Student

User = get_user_model() 

class CourseAPITestCase(APITestCase):
    def setUp(self):
        user_obj = User(username='sven', email='sven@live.com')
        user_obj.set_password("sup3r$3cr37")        #superSecret
        user_obj.save()
        
        course_post = Course.objects.create(
            Description = 'Some Description',
            Code = 234,
            Professor = 'Dr Scratchnsniff',
            Capacity = 15    
        )

    # first test, make sure we can add a user 
    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_course(self):
        count = Course.objects.count()
        self.assertEqual(count, 1)

    def test_zero_student(self):
        count = Student.objects.count()
        self.assertEqual(count, 0)

    def test_two_student(self):
        student_obj = Student(
            Name = 'FriendlyRadio UnitTester',
            StudentId = 1234,
        )
        student_obj.save()
        student2_obj = Student(
            Name = 'Another FriendlyRadio UnitTester',
            StudentId = 12345,
        )
        student2_obj.save()

        count = Student.objects.count()
        self.assertEqual(count, 2)
        print('\n\r --- START print to screen ---')
        print(student_obj.Name)
        print(' --- STOP print to screen ---')

    #delete a student
    #def test_remove_student(self):
    #    #student_obj = Student.objects.get('Another FriendlyRadio UnitTester')
    #    student_obj = Student.objects.last()
    #    student_obj.delete()
    #    count = Student.objects.count()
    #    self.assertEqual(count, 1)

    def test_student_enrollment(self):
        pass
        # need to figure out how to do this unit test in Django


