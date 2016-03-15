READ ME: Setting up Chicago Pothole Repair Tracker
by Jose Murillo and Jenny Xu

We have reduced setting up the code to 3 simple steps.
In this file, you'll see "directory". This indicates the
directory where you need to run the necessary code.
"CODE" indicates the code that needs to be run in the command line

Enjoy!

***** Step 1: Download Data *****
    Directory: chicago_potholes/project/potholes_site

    CODE:
    python3 download_data.py

    Note: The program above will open your web browser with a url
        that will download the data to your computer. A pop up
        might appear asking you to save the data. Select "Save to". 
        The file will be saved to Home/Downloads. Move it to the directory chicago_potholes/project/potholes_site.

***** Step 2: Constructing Database ~ 60 minutes *****
Two approaches:
    1) Run execute.py and it will complete all the tasks
    Directory: chicago_potholes/project/potholes_site

    CODE: 
    python3 execute.py <pothole_csv_filename>


OR 

    2) Run each of these files separately
    Directory: chicago_potholes/project/potholes_site

    CODE:
    python3 potholes.py <csv_filename>
    python3 traffic.py
    python3 aldermen.py
    python3 update.py chicago.db

    Note: Depending on the sample size, all of the code might take
        up to an hour to run.


***** Step 3: Runserver to see website *****
Directory: chicago_potholes/project

CODE:
python3 manage.py runserver

---------------------------------------------------------------------------

Everything is original work unless noted otherwise

Credits:
https://automatetheboringstuff.com/chapter16/
http://stackoverflow.com/questions/811548/sqlite-and-python-return-a-dictionary-using-fetchone
https://developers.google.com/maps/documentation/javascript/examples/marker-simple
https://developers.google.com/maps/documentation/javascript/examples/marker-animations-iteration
http://gis.stackexchange.com/a/56589/15183
http://stackoverflow.com/questions/403421/how-to-sort-a-list-of-objects-in-python-based-on-an-attribute-of-the-objects



List of Modules:
sqlite3
sys
json
math
statistics
datetime
smtplib
os
django
csv
request
re


*********************************************

HOW IT WORKS:

//////////////////////////////////////////////////
Creating Database:

Pothole data is downloaded as a csv file, which is moved into a SQL table in chicago.db using potholes.py

traffic.py and alderman.py take in data from their respective APIs, and convert the data to SQL tables in chicago.db

All data is converted to Python class objects (using classes.py), and update.py updates the pothole class objects with traffic count and urgency level (which is calculated using traffic count). The potholes SQL table is updated with these modifications. 

///////////////////////////////////////
Website:

Our website has 3 pages:
Home page: displays a map with markers representing potholes. 
Animation page: animates potholes over a period of time specified by user using the search tool
Stats page: displays side-by-side statistics for pothole data in 3 different wards, based on user input

Home page:
1) User enters and submits search criteria, which is sent to views.py as a POST method. 
2) The search criteria is converted to a SQL query using search.py, and the query returns the appropriate pothole data as pothole objects
3) Pothole objects are converted to JSON form and sent to the webpage
JSON data is used to create markers

Extra features:
1) If the pothole is open, the program creates a form. 
2) The information from the form is used to create the appropriate Alderman object
3) Alderman has an email function that is called upon


Animation Page:
1) User enters and submits search criteria, which is sent to views.py as a POST method. 
2) The search criteria is converted to a SQL query using search.py, and the query returns the appropriate pothole data as pothole objects
3) Pothole objects are converted to JSON form and sent to the webpage
4) JSON data is used to create the animation
5) Animation is made by making markers appear at 200ms times the day the pothole is reported and vanishing at 200ms times the day the pothole is completed

Stats page
1) User enters and submits search criteria, which is sent to views.py as a POST method. 
2) The search criteria is converted to a SQL query using search.py, and the query returns the appropriate pothole data as pothole objects:
3) StatWard object is created which compiles various statistics of the ward into a simple object
4) StatWard objects are converted to JSON form and sent to the webpage
5) JSON data is used to create tables of statistics


