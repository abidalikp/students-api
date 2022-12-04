from rest_framework import serializers

from api import models

# Create your serializers here

# Major Serializer
class MajorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Major
        fields = '__all__'

# Course Serializer
class CourseSerializer(serializers.ModelSerializer):

    major = MajorSerializer(read_only=True)

    class Meta:
        model = models.Course
        fields = '__all__'

# Student Serializer
class StudentSerializer(serializers.ModelSerializer):

    major = MajorSerializer(read_only=True)

    class Meta:
        model = models.Student
        fields = '__all__'

# Student Course Serializer
class StudentCourseSerializer(serializers.ModelSerializer):

    student = StudentSerializer(read_only=True)
    course = CourseSerializer(read_only=True)

    class Meta:
        model = models.StudentCourse
        fields = '__all__'