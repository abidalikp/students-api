from rest_framework import serializers

from api import models

# Create your serializers here

class InstituteSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Institute
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):

    institute = InstituteSerializer(read_only = True)

    class Meta:
        model = models.Student
        fields = '__all__'