from django.shortcuts import render
from django.forms import ModelForm
from potholes_site.models import *


class SearchForm(ModelForm):
    class Meta:
        model = Search 
        fields = ['status', 'start_date', 'end_date', 'zip_code', 'urgency']

class StatForm(ModelForm):
    class Meta:
        model = Stat
        fields = ['Neighborhood_1', 'Neighborhood_2', 'Neighborhood_3']

def main_page(request):
    c = {'model':SearchForm()}
    return render(request, "potholes_site/main.html",c)

def stats(request):
    c = {'model':StatForm()}
    return render(request, "potholes_site/stats.html", c)

