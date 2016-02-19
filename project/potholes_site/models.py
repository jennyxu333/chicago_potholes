from django.db import models
from django.forms import ModelForm

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
    start_date = models.DateField(default='MM/DD/YYYY')
    end_date = models.DateField(default='MM/DD/YYYY')
    zip_code = models.IntegerField(default=60637)
    urgency = models.ForeignKey('Urgency', null=True)

class Neighborhood1(models.Model):
    name = models.CharField(max_length = 20)
    # default is geo location 

class Neighborhood2(models.Model):
    name = models.CharField(max_length = 20)

class Neighborhood3(models.Model):
    name = models.CharField(max_length = 20)

class Stat(models.Model):
    Neighborhood_1 = models.ForeignKey('Neighborhood1')
    Neighborhood_2 = models.ForeignKey('Neighborhood2')
    Neighborhood_3 = models.ForeignKey('Neighborhood3')
