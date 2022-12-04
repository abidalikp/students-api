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

    class Meta:
        model = models.Course
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['major'] = MajorSerializer()
        return super().to_representation(instance)

# Student Serializer
class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Student
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['major'] = MajorSerializer(read_only=True)
        return super().to_representation(instance)

# Student Course Serializer
class StudentCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StudentCourse
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['student'] = StudentSerializer(read_only=True)
        self.fields['course'] = CourseSerializer(read_only=True)
        return super().to_representation(instance)
