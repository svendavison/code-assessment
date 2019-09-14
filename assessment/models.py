from django.db import models

class Courses(models.Model):
    Description = models.CharField(max_length=200)
    Code = models.IntegerField()
    Professor = models.CharField(max_length=200)
    Capacity = models.IntegerField()

    def __str__(self):
        return self.Description

    class Meta:
        verbose_name = "Course"


class Students(models.Model):
    Name = models.CharField(max_length=200)
    StudentId = models.IntegerField()
    
    def __str__(self):
        return self.Name
    
    class Meta:
        verbose_name = "Student"
    #    verbose_name_plural = "Student"


#Create an application that provides a simple Web UI or API that allows users to:
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

# The back-end should be implemented in Python and support the front end via 
# ReST endpoints using Django or Flask (preferably). The data model shall be
#  maintained in either (or some combination of) MariaDB/MySQL, sqlite, or 
# MongoDB. However you see fit. I will test functionality with curl calls..

 # Ahmad Soliman <Ahmad.Soliman@bridges-inc.com>
