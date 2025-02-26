from django.db import models
from django.contrib.auth.models import User

class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    marks = models.IntegerField()
    class_name = models.CharField(max_length=100)
    semester = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    nationality = models.CharField(max_length=100)
    grade = models.CharField(max_length=2)
    section = models.CharField(max_length=10)
    topic = models.CharField(max_length=100)
    stage = models.CharField(max_length=100)
    absent_days = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.class_name}"


# ---------------TEACHER DETAILS ADD MODEL---------------
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    experience = models.IntegerField(help_text="Years of experience")
    phone = models.CharField(max_length=15)
    address = models.TextField()

    # def __str__(self):
    #     return self.user.first_name

