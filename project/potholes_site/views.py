from django.shortcuts import render
from django.forms import ModelForm
from potholes_site.models import *


# Create your views here.


class SearchForm(ModelForm):
    class Meta:
        model = Search 
        fields = ['status', 'start_date', 'end_date', 'zipcode']

def main_page(request):
    c = {'model':SearchForm()}
    return render(request, "potholes_site/map.html",c)