from django.db import models
from django.forms import ModelForm

# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length = 10)

class Ward(models.Model):
    name = models.IntegerField()

class Urgency(models.Model):
    name = models.CharField(max_length = 10)

class Search(models.Model):
    status = models.ForeignKey('Status')
    #start_year = models.IntegerField(max_length = 4)
    #start_month = models.IntegerField(max_length = 2)
    #start_day = 
    start_date = models.DateField()
    end_date = models.DateField()
    zipcode = models.IntegerField(default=60637)
