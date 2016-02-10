import csv
import json

class Pothole(object):

    def __init__(self, creation_date, status, completion_date, service_num,\
     current_activity,action, potholexblock, street, zip, ward, community, \
     lat, lon):
        self.creation_date = creation_date






def open_csv():
    l = open("pothole_data.csv")
    j = l.readlines()
    l.close()

    dictionary ={}
    for i in j[0]:
        if i != "\n":
            i = i.rstrip()
            i = i.split(",")
            print(i)


csvfile = open('pothole_data.csv', 'r')
j = csvfile.readlines()

fieldnames = []
l = j[0].split(",")
l[-1] = l[-1][:-1]
for i in l:
    fieldnames.append(i)

reader = csv.DictReader(csvfile, fieldnames=tuple(fieldnames))
print(reader)
out = json.dumps([row for row in reader])
print(out)
jsonfile = open('pothole_data.json', 'w')
jsonfile.write(out)

csvfile.close()
jsonfile.close()