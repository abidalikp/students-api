from django.urls import path

from api import views

urlpatterns = [
    path('students', views.StudentAPI.as_view()),
    path('students/<int:pk>/courses', views.StudentCoursesAPI.as_view()),
    path('students/<int:pk>', views.StudentDetailAPI.as_view()),
    path('majors', views.MajorAPI.as_view()),
    path('majors/<int:pk>', views.MajorDetailAPI.as_view()),
    path('majors/<int:pk>/courses', views.MajorCoursesAPI.as_view()),
    path('majors/<int:pk>/students', views.MajorStudentsAPI.as_view()),
    path('courses', views.CourseAPI.as_view()),
    path('courses/<int:pk>', views.CourseDetailAPI.as_view()),
    path('courses/<int:pk>/students', views.CourseStudentsAPI.as_view()),
    path('studentcourses', views.StudentCourseAPI.as_view()),
]