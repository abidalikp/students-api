from django.db import models

# Create your models here.


# Majors
class Major(models.Model):
    
    name = models.CharField(max_length = 50, unique=True)

    def __str__(self):
        return self.name

# Courses
class Course(models.Model):

    name = models.CharField(max_length = 50, unique=True)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Students
class Student(models.Model):

    GENDERS = (
        ('u', 'undisclosed'),
        ('f', 'female'),
        ('m', 'male')
    )

    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    roll_number = models.IntegerField(unique = True)
    gender = models.CharField(max_length = 1, choices = GENDERS)
    gpa = models.FloatField()
    major = models.ForeignKey(Major, on_delete=models.SET_NULL, null=True, blank=True, default=None)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

# Courses of Students
class StudentCourse(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='courses')
    mark = models.FloatField(blank=True, null=True, default=None)

    def __str__(self):
        return "{} - {}".format(self.student, self.course)
