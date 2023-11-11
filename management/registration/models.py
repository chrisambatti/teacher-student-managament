from django.db import models

# Create your models here.

class StudentDetails(models.Model):
    username = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    emailId = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    
class TeacherDetails(models.Model):
    username = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    emailId = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    
class TeacherAssignment(models.Model):
    assignmentname = models.CharField(max_length=255)
    assignmentdetails = models.CharField(max_length=255)
    classdetails = models.CharField(max_length=255)
        