from django.contrib import admin

from .models import Courses
from .models import Students

admin.site.register(Courses)
admin.site.register(Students)