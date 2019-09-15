from django.db import models

class Course(models.Model):
    Description = models.CharField(max_length=50)
    Code = models.IntegerField()
    #professor should be another table in another relationship for data normaliation
    Professor = models.CharField(max_length=50) 
    Capacity = models.IntegerField()

    def __str__(self):
        return self.Description
    

# class CourseRegistration(models.Model):
#    Name = models.CharField(max_length=50)
#    #StudentName = models.ForeignKey(Student, on_delete=models.CASCADE)
#    CourseId = models.ForeignKey(Course, on_delete=models.CASCADE)
#
#    def __str__(self):
#        return self.Name
    

# done but needs testing for 2.0
class Student(models.Model):
    Name = models.CharField(max_length=50)
    StudentId = models.IntegerField()
    Courses = models.ManyToManyField(Course)

    class Meta:
        verbose_name = ("Student")
        verbose_name_plural = ("Students")

    def __str__(self):
        return self.Name

