from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from api import models, serializers

# Create your views here.

# Students
class StudentList(ListCreateAPIView):
    # permission_classes = [IsAdminUser]
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

class StudentDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
# Majors
class MajorList(ListCreateAPIView):
    queryset = models.Major.objects.all()
    serializer_class = serializers.MajorSerializer

class MajorDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = models.Major.objects.all()
    serializer_class = serializers.MajorSerializer

# Courses
class CourseList(ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

class CourseDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

# Major Courses

# Student Courses