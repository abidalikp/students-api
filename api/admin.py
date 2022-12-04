from django.contrib import admin

from api import models

# Register your models here.

admin.site.register([
    models.Student,
    models.StudentCourse,
    models.Course,
    models.Major,
    models.MajorCourse,
])