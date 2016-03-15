import csv
import sqlite3
import re
import datetime
import sys

# Column header indices - DO NOT MODIFY
CREATION_DATE = 0
STATUS = 1
COMPLETION_DATE = 2
SERVICE_NUM = 3
CURRENT_ACTIVITY = 5
MOST_RECENT_ACTION = 6
NUM_POTHOLES_BLOCK = 7
STREET_ADDRESS = 8
ZIP = 9
WARD = 12
LATITUDE = 16
LONGITUDE = 17

def open_csv(filename):
    '''
    Opens the csv file and returns the data as a list of rows (minus header)
    '''
    f = open(filename)
    lines = f.readlines()
    f.close()

    return lines[1:]


def go(filename):
    '''
    Creates a table called Potholes in chicago.db
    '''
    data = open_csv(filename)

    conn = sqlite3.connect('chicago.db')
    cur = conn.cursor()

    create = '''CREATE TABLE potholes (creation_date DATE, status TEXT, 
                completion_date DATE, response_time VARCHAR, 
                service_request_number TEXT, 
                current_activity TEXT, most_recent_action TEXT, 
                number_of_potholes_filled_on_block NUMBER, street_address TEXT, 
                zip NUMBER, ward NUMBER, latitude NUMBER, longitude NUMBER, 
                urgency TEXT, traffic NUMBER, street VARCHAR)'''

    cur.execute("DROP TABLE IF EXISTS potholes")
    cur.execute(create)

    insert = '''INSERT INTO potholes VALUES (%s)''' %('?,'*15 + '?')

    for row in data:
        row = row.split(',')

        # ignore data points that are missing coordinates
        if row[LATITUDE] != '' and row[LONGITUDE] != '':
            d = row[CREATION_DATE].split('/')
            year = int(d[2])
            month = int(d[0])
            day = int(d[1])
            creation_date = datetime.datetime(year, month, day)
            creation_date = creation_date.date()

            # response time is equal to number of days between creation date 
            # and completion date
            if row[COMPLETION_DATE] != "":
                d = row[COMPLETION_DATE].split('/')
                year = int(d[2])
                month = int(d[0])
                day = int(d[1])
                completion_date = datetime.datetime(year, month, day)
                completion_date = completion_date.date()
                response_time = completion_date - creation_date
                response_time = response_time.days
            else:
                completion_date = row[COMPLETION_DATE]
                response_time = "__"

            if row[STREET_ADDRESS] == '0' or row[STREET_ADDRESS] == '':
                street_address = ""
                street = ""
            else:
                street_address = row[STREET_ADDRESS]

                # extract street name from the address
                find = re.search('(^\d+\s[NSEW]\s)([\w\s]+)', street_address)
                street = find.groups()[1]

            
                latitude = row[LATITUDE]
                longitude = row[LONGITUDE]


            # traffic count and urgency level have default value 0
            args = [creation_date, row[STATUS], completion_date, response_time,\
                    row[SERVICE_NUM], row[CURRENT_ACTIVITY], row[MOST_RECENT_ACTION],\
                    row[NUM_POTHOLES_BLOCK], row[STREET_ADDRESS], row[ZIP], row[WARD],\
                    latitude, longitude,0,0,street]

            cur.execute(insert, args)

    conn.commit()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python3 {} <pothole csv file>".format(sys.argv[0]))
        sys.exit(1)

    go(sys.argv[1])

    