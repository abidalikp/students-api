from django.urls import path

from api import views

urlpatterns = [
    path('students', views.StudentList.as_view()),
    path('students/<int:pk>', views.StudentDetailsView.as_view()),
    path('majors', views.MajorList.as_view()),
    path('majors/<int:pk>', views.MajorDetailsView.as_view()),
    path('courses', views.CourseList.as_view()),
    path('courses/<int:pk>', views.CourseDetailsView.as_view()),
]