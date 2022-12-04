from rest_framework.response import Response
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from api import models, serializers

# Create your views here.

# Students
class StudentAPI(ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

class StudentDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    
# Majors
class MajorAPI(ListCreateAPIView):
    queryset = models.Major.objects.all()
    serializer_class = serializers.MajorSerializer

class MajorDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = models.Major.objects.all()
    serializer_class = serializers.MajorSerializer

# Courses
class CourseAPI(ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

class CourseDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

# Student Courses
class StudentCourseAPI(ListCreateAPIView):
    queryset = models.StudentCourse.objects.all()
    serializer_class = serializers.StudentCourseSerializer