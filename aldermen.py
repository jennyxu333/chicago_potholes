import requests
import sqlite3

r = requests.get("https://data.cityofchicago.org/resource/htai-wnw4.json",\
                    headers={"X-App-Token":"GPTaI6SMKDSNWfCGLg22yOXV8"})

headers = []
for key in r.json()[0]:
    headers.append(key)

print(headers)

conn = sqlite3.connect('chicago.db')
cur = conn.cursor()

create = "CREATE TABLE aldermen (alderman VARCHAR, ward INTEGER, email VARCHAR)"

cur.execute("DROP TABLE IF EXISTS aldermen")
cur.execute(create)

insert = "INSERT INTO aldermen VALUES (?, ?, ?)"

for d in r.json():
    alderman = d["alderman"]
    ward = d["ward"]
    email = d["email"]

    args = [alderman, ward, email]
    cur.execute(insert, args)

conn.commit()

r = cur.execute("SELECT * FROM aldermen")
r = r.fetchall()

conn.close()