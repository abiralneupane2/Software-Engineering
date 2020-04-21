from django.db import models
from django.contrib.auth.models import User
from django import forms




class department(models.Model):
    department_name=models.CharField(max_length=50)
    object=models.Manager()

    def __str__(self):
        return self.department_name


class student_data(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.IntegerField(null=True)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    #teacher_name = forms.ChoiceField(choices=DEPARTMENTS)
    aggregate_percentage = models.IntegerField()
    project_details = models.CharField(max_length=1000, null=True)
    publication_details = models.CharField(max_length=1000, null=True)
    eca_details = models.CharField(max_length=1000,null=True)
    university_to_address = models.CharField(max_length=100)
    deadline = models.DateField()
    object=models.Manager()

    def __str__(self):
        return self.name
