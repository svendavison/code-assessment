from django.urls import path, include
from . import views
from rest_framework import routers

# similar to obect based url building
router = routers.DefaultRouter()
router.register('student', views.StudentView)
router.register('courses', views.CourseView)
#router.register('registrations', views.CourseRegistrationView)

urlpatterns = [
    path('', include(router.urls))
]
