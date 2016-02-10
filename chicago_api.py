import requests
import sqlite3
import datetime

r = requests.get("https://data.cityofchicago.org/resource/7as2-ds3y.json", \
                    headers={"X-App-Token":"GPTaI6SMKDSNWfCGLg22yOXV8"})

ph_headers = []
for key in r.json()[0]:
    ph_headers.append(key)

#print("HEADERS:", ph_headers)

conn = sqlite3.connect('chicago.db')
cur = conn.cursor()

args1 = ("creation_year" , "creation_month",
            "creation_day", "status", "completion_year",
            "completion_month", "completion_day", "response_time",
            "service_request_number", "current_activity", 
            "most_recent_action", "number_of_potholes_filled_on_block", 
            "street_address", "zip", "ward", "community_area", 
            "latitude", "longitude")

insert = '''INSERT INTO potholes'''+ str(args1) + '''VALUES (%s)''' %('?,'*17 + '?')

for d in r.json():
    #d = r.json()[20]
    creation_date = d['creation_date']
    creation_year = int(creation_date[:4])
    creation_month = int(creation_date[5:7])
    creation_day = int(creation_date[8:10])
    creation_date = datetime.datetime(creation_year, creation_month, \
        creation_day)

    if 'completion_date' in d:
        completion_date = d['completion_date']
        completion_year = int(completion_date[:4])
        completion_month = int(completion_date[5:7])
        completion_day = int(completion_date[8:10])
        completion_date = datetime.datetime(completion_year, completion_month,\
            completion_day)
        response_time = completion_date - creation_date
    else:
        completion_year = ''
        completion_month = ''
        completion_day = ''
        current_date = datetime.datetime.now()
        response_time = current_date - creation_date
    response_time = response_time.days

    current_activity = d.get('current_activity', '')
    most_recent_action = d.get('most_recent_action', '')
    num_ph_filled = d.get('number_of_potholes_filled_on_block', 0)
    zipcode = d.get('zip', 0)
    ward = d.get('ward', '')
    community_area = d.get('community_area', '')

    args2 = [creation_year, creation_month, creation_day, d['status'], \
            completion_year, completion_month, completion_day, \
            response_time, d['service_request_number'], current_activity, \
            most_recent_action, num_ph_filled, d['street_address'], \
            zipcode, ward, community_area, d['latitude'], d['longitude']]
    #print(args2)
    r = cur.execute(insert,args2)
conn.commit()

r = r.fetchall()
conn.close()
