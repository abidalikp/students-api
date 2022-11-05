from django.urls import path

from api import views

urlpatterns = [
    path('students', views.StudentList.as_view()),
    path('students/<int:pk>', views.StudentDetailsView.as_view())
]