from django.shortcuts import render
from django.forms import ModelForm
from potholes_site.models import *
from django import forms
from potholes_site.classes import *
from potholes_site.update import *
from potholes_site.search import *
from potholes_site.stats import *
import datetime

class SearchForm(ModelForm):
    class Meta:
        model = Search 
        fields = ['status', 'start_date', 'end_date', 'zip_code', 'urgency']

class AnimateForm(ModelForm):
    class Meta:
        model = Search
        fields = ['start_date', 'end_date', 'zip_code', 'urgency']

class StatForm(ModelForm):
    class Meta:
        model = Stat
        fields = ['Ward_1', 'Ward_2', 'Ward_3']

class EmailForm (ModelForm):
    class Meta:
        model = Email
        fields = ['ward']


def format_date(string):
    '''
    Takes a date string, and converts it into a datetime object
    '''
    l = string.split('-')
    date = datetime.date(int(l[0]),int(l[1]), int(l[2]))
    return date


def main_page(request):
    '''
    Runs when the main webpage is opened
    '''
    db = 'potholes_site/chicago.db'

    # Default potholes to show on map upon opening the webpage
    query = '''SELECT * FROM potholes WHERE 
            (creation_date >= date(julianday(date('now'))-7) OR 
            completion_date >= date(julianday(date('now'))-7)) AND
            zip = 60637'''
    args = None
    ward_num = None
    ph = main(query, db, args)

    print(ph)

    c = {'model':SearchForm(), 'model1':EmailForm(), 'ph':ph}

    # if user enters search criteria and clicks 'Search':
    if request.method == "POST":
        search_query = request.POST
        query, args = find_potholes(search_query)
        # ph: a list of potholes that match the search criteria, represented as 
        # dictionaries
        ph = main(query, db, args)
        c = {'model':SearchForm(), 'model1':EmailForm(), 'ph':ph}

    now = datetime.date.today()
    for pothole in ph:
        if pothole['status'] == 'Open':
            report = format_date(pothole['creation_date'])
            pothole['response_time'] = (now - report).days
    
    # handles inputs from the email function
    if request.method == "GET":
        search_query = request.GET
        if 'ward' in search_query and 'message' in search_query:
            ward_num = search_query['ward']
            message = search_query['message']
            email_ward(ward_num, message, db)
            print("Email sent")
            c = {'model':SearchForm(), 'model1':EmailForm(), "sent" : "True"}
            return render(request, "potholes_site/home.html",c)
    
    return render(request, "potholes_site/home.html",c)


def animation(request):
    '''
    Runs when the animation webpage is opened
    '''
    db = 'potholes_site/chicago.db'
    query = '''SELECT * FROM potholes WHERE 
            (creation_date >= date(julianday(date('now'))-30) OR 
            completion_date >= date(julianday(date('now'))-30)) AND
            zip = 60637'''
    args = None
    
    c = {'model':AnimateForm(), 'ph':main(query, db, args)}

    if request.method == "POST":
        search_query = request.POST
        query, args = find_potholes(search_query)

        baseline = format_date(search_query['start_date'])

        # ph: a list of potholes that match the search criteria, represented as 
        # dictionaries
        ph = main(query, db, args)

        for pothole in ph:
            opened = format_date(pothole['creation_date'])
            if pothole['completion_date'] == '' or \
                pothole['completion_date'] > search_query['end_date']:
                closed = format_date(search_query['end_date'])
            else:
                closed = format_date(pothole['completion_date'])

            '''
            create new dictionary keys for pothole:
                day: number of days between the pothole's report date and the
                        start date selected by user
                close: number of days between the pothole's completion date and
                        the start date selected by user
            '''
            diff_open = (opened - baseline).days
            pothole['day'] = pothole.get('day', diff_open)

            diff_close = (closed - baseline).days
            pothole['close'] = pothole.get('close', diff_close)

        c = {'model':AnimateForm(), 'ph':ph}
 
    print("potholes:", main(query, db, args))
    

    return render(request, "potholes_site/animate.html",c)


def stats(request):
    '''
    Runs when the comparative statistics webpage is opened
    '''
    db = 'potholes_site/chicago.db'
    c = {'model':StatForm()}

    if request.method == "POST":
        inputs = request.POST
        ward_method = []
        for key in inputs:
            if key == "Ward_1" or key == "Ward_2" or key == "Ward_3" :
                ward_method.append(inputs[key])
        c = {'model':StatForm(), 'wards':stat_dict(ward_method, db)}

    return render(request, "potholes_site/stats.html", c)


