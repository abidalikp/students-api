from django.db import models

# Create your models here.

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

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

# Majors
class Major(models.Model):
    
    major = models.CharField(max_length = 50, unique=True)

    def __str__(self):
        return self.major

# Courses
class Course(models.Model):

    course = models.CharField(max_length = 50, unique=True)

    def __str__(self):
        return self.course
    
# Courses in each Major
class MajorCourse(models.Model):

    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.major, self.course)

# Courses of Students
class StudentCourse(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.student, self.course)
