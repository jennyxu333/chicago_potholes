import requests
import sqlite3

r = requests.get("https://data.cityofchicago.org/resource/pfsx-4n4m.json",\
                    headers={"X-App-Token":"GPTaI6SMKDSNWfCGLg22yOXV8"})

headers = []
for key in r.json()[0]:
    headers.append(key)

print(headers)

conn = sqlite3.connect('chicago.db')
cur = conn.cursor()

create = '''CREATE TABLE traffic (id NUMBER, count_location TEXT, 
            street TEXT, total_passing_volume NUMBER, 
            volume_by_direction TEXT, latitude NUMBER, longitude NUMBER)'''

cur.execute("DROP TABLE IF EXISTS traffic")
cur.execute(create)

insert = "INSERT INTO traffic VALUES (?, ?, ?, ?, ?, ?, ?)"

print(r.json()[0])
for d in r.json():
    ID = d['id']
    count_location = d['traffic_volume_count_location_address']
    street = d['street']
    total_passing_volume = d['total_passing_vehicle_volume']
    volume_by_direction = str(d['vehicle_volume_by_each_direction_of_traffic'])
    latitude = d['latitude']
    longitude = d['longitude']

    args = [ID, count_location, street, total_passing_volume, \
            volume_by_direction, latitude, longitude]

    cur.execute(insert, args)

conn.commit()

r = cur.execute("SELECT * FROM traffic")
r = r.fetchall()

conn.close()
