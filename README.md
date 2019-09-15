# Code Assessment

This is a repo of a code assessment I had to do. It turns out, the Django Rest Framework is wonderful and makes things A LOT easier. I still need to create/modify the REST endpoints to be more specific which I hope to figure out by tomorrow.

# Tools Used
* Django
* Django Rest Framework
* Visual Studio Code (on a MacBookPro)

# Pip Freeze report
* (venv1) svenMacBook:api_example svendavison$ pip freeze
* Django==2.2.5
* djangorestframework==3.10.3
* pytz==2019.2
* sqlparse==0.3.0

# The Assessment Tasks
* Create an application that provides a simple Web UI or API that allows users to:
* CRUD* Courses w/
  * Description
  * Code
  * Professor
  * Capacity
* CRUD Students w/
  * Name
  * Student Id
* ReST end points w/
  * Assign student to course
    * ../student/enroll/<course id>
  * Remove a student from a course
    * ../student/drop/<course id>
  * Fetch all students in a course
    *  ../course/students
  * Fetch students
    * ../student/all
  * Fetch all courses
    * ../course/all

# Additional requirements for the assessment.
The back-end should be implemented in Python and support the front end via ReST endpoints using Django or Flask (preferably). The data model shall be maintained in either (or some combination of) MariaDB/MySQL, sqlite, or MongoDB. However you see fit. I will test functionality with curl calls.
