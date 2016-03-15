from django.db import models
from django.forms import ModelForm
from django import forms

STATUS_CHOICES = (
            ('Open', 'Not repaired'), 
            ('Completed','Repaired'))

URGENCY_CHOICES = (
            ('Very Low','Very Low'),
            ('Low','Low'),
            ('Medium','Medium'),
            ('High','High'),
            ('Very High','Very High'))


class Search(models.Model):
    '''
    Creates the fields that the user is able to filter their search by in the
    main page.
    '''
    status = models.CharField(max_length=10,choices=STATUS_CHOICES)
    start_date = models.DateField(default='YYYY-MM-DD')
    end_date = models.DateField(default='YYYY-MM-DD')
    zip_code = models.IntegerField(default=60637)
    urgency = models.CharField(max_length=10,choices=URGENCY_CHOICES)


class Animate(models.Model):
    '''
    Creates the fields that the user is able to filter their search by in the
    animation page.
    '''
    start_date = models.DateField(default='2016-01-01')
    end_date = models.DateField(default='2016-03-08')
    zip_code = models.IntegerField(default=60637)
    urgency = models.CharField(max_length=10,choices=URGENCY_CHOICES)


class Stat(models.Model):
    '''
    Creates three empty input fields for the user to enter three wards for 
    comparison.
    '''
    Ward_1 = models.CharField(max_length=2)
    Ward_2 = models.CharField(max_length=2)
    Ward_3 = models.CharField(max_length=2)


class Email(models.Model):
    ward = models.IntegerField()
