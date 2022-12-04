from rest_framework import serializers

from api import models

# Create your serializers here

# Course Serializer
class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Course
        fields = '__all__'

# Major Serializer
class MajorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Major
        fields = '__all__'

# Student Serializer
class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Student
        fields = '__all__'