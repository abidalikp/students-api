from django.db import models

# Create your models here.

class Student(models.Model):

    GENDERS = (
        ('u', 'undisclosed'),
        ('f', 'female'),
        ('m', 'male')
    )

    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    roll_number = models.IntegerField(unique = True)
    gender = models.CharField(max_length = 1, choices = GENDERS)
    percentage = models.FloatField()

    institute = models.ForeignKey('Institute', on_delete = models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.name

class Institute(models.Model):

    TYPES = (
        ('c', 'College'),
        ('s', 'School')
    )
    
    name = models.CharField(max_length = 100)
    type = models.CharField(max_length = 1, choices = TYPES)

    def __str__(self):
        return self.name