from rest_framework.response import Response
from rest_framework.generics import (
    # ListAPIView,
    # RetrieveAPIView,
    # UpdateAPIView,
    # RetrieveUpdateAPIView,
    # DestroyAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from api import models, serializers

# Create your views here.

class StudentList(ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

class StudentDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer