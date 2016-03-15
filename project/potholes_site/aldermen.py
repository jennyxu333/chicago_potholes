import requests
import sqlite3

def go():
    '''
    Creates the alderman table in chicago.db
    '''
    # obtain aldermen data as a list of dictionaries 

    r = requests.get("https://data.cityofchicago.org/resource/htai-wnw4.json",\
                        headers={"X-App-Token":"GPTaI6SMKDSNWfCGLg22yOXV8"})

    # create the table
    conn = sqlite3.connect('chicago.db')
    cur = conn.cursor()

    create = "CREATE TABLE aldermen (alderman VARCHAR, ward INTEGER, email VARCHAR)"

    cur.execute("DROP TABLE IF EXISTS aldermen")
    cur.execute(create)

    insert = "INSERT INTO aldermen VALUES (?, ?, ?)"

    # iterate over each data point, represented by a dictionary
    for d in r.json():
        alderman = d["alderman"]
        ward = d["ward"]
        email = d["email"]

        args = [alderman, ward, email]
        cur.execute(insert, args)

    conn.commit()

    conn.close()


if __name__ == "__main__":
    go()