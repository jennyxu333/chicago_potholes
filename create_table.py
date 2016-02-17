import sqlite3

conn = sqlite3.connect('chicago.db')
cur = conn.cursor()

create = '''CREATE TABLE potholes (creation_year VARCHAR, creation_month VARCHAR,
            creation_day VARCHAR, status TEXT, completion_year VARCHAR,
            completion_month VARsCHAR, completion_day VARCHAR, response_time NUMBER,
            service_request_number TEXT, current_activity TEXT, 
            most_recent_action TEXT, number_of_potholes_filled_on_block NUMBER, 
            street_address TEXT, zip NUMBER, ward NUMBER, community_area NUMBER, 
            latitude NUMBER, longitude NUMBER)'''

cur.execute('DROP TABLE IF EXISTS potholes')
cur.execute(create)