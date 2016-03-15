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
