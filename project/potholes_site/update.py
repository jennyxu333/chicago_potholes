import sqlite3
import json
try:
    from classes import *
except:
    from potholes_site.classes import *
import math
import sys

SIDE_TRAFFIC = 0.1

def go(db):
    '''
    Updates pothole database using alderman data

    Inputs:
        db: database name
    '''
    query1 = "SELECT * FROM potholes WHERE creation_date >= '2016-01-01'"
    query2 = "SELECT * FROM traffic"
    modify_and_update_potholes(query1, query2, 1, db)

def modify_and_update_potholes(pot_query, traf_query, max_dist, db):
    '''
    Updates the potholes

    Inputs:
        pot_query: string of the query used to find the potholes
                that need to be updated
        traf_query: string of the query used to find the traffic
        max_dist: maximum acceptable distance between traffic point
                and pothole
        db: databse name

    '''
    print("Process might take up to an hour.")
    print("Starting Process!")
    print()
    print()
    print("Step 1 of 7: Creating Dicionary of Potholes")
    pot_dict = create_query_dict(pot_query, db)
    print("Step 2 of 7: Creating Pothole Objects")
    pot_object = create_pothole(pot_dict)
    print("Step 3 of 7: Creating Dictionary of Traffic")
    traf_dict = create_query_dict(traf_query, db)
    print("Step 4 of 7: Creating Traffic Objects")
    traf_object = create_traffic(traf_dict)
    print("Step 5 of 7: Updating Potholes with Traffic Count")
    Traffic_Pothole(pot_object, traf_object, max_dist) 
    print("Step 6 of 7: Updating Potholes with Urgency")
    Status(pot_object)
    print("Step 7 of 7: Pushing Modified Potholes into Database")
    Update_Potholes(pot_object, db)
    print("Everything is completed. Have a great day!")

def create_query_dict(query, db, args=None):
    '''
    Creates a dictionary from a query

    Inputs: 
        query: query for database
        db: database name
        args: (optional) arguments for query

    Returns:
        r: results from query
    '''
    con = sqlite3.connect(db)
    con.row_factory = dict_factory
    cur = con.cursor()
    if args == None:
        cur.execute(query)
    else:
        cur.execute(query,args)
    r = cur.fetchall()
    con.close()
    return r

def create_pothole(r):
    '''
    Creates a list of potholes

    Input:
        r: results from query

    Returns:
        pothole_list: list of pothole object

    '''
    pothole_list =[]
    for i in r:
        pothole_list.append(Pothole(i["creation_date"], i["status"], \
            i["completion_date"], i["response_time"], 
            i["service_request_number"], \
            i["current_activity"], i["most_recent_action"], \
            i["number_of_potholes_filled_on_block"], i["street_address"],\
            i["zip"], i["ward"], i["latitude"], \
            i["longitude"], i["urgency"], i["traffic"], i["street"]))
    return pothole_list

def create_traffic(r):
    '''
    Creates a list of traffic objects

    Input:
        r: results from query

    Returns:
        traffic_list: list of Traffic objects

    '''
    traffic_list = []
    for i in r:
        traffic_list.append(Traffic(i["id"], i["count_location"], i["street"], \
            i["total_passing_volume"], i["volume_by_direction"],\
            i["latitude"], i["longitude"]))

    return traffic_list

def Traffic_Pothole(pothole, traffic, max_dist):
    '''
    Finds the traffic passing through a pothole and updates the
    Pothole object

    Inputs:
        pothole: list of potholes objects
        traffic: list of traffic objects
        max_dist: maximum acceptable distance between traffic 
                point and pothole

    Returns:
        list of potholes with modified traffic count
    '''

    for hole in pothole:
        for traf in traffic:
            if hole.distance_traffic(traf.latitude, traf.longitude) \
                < max_dist:

                if hole.street_only == traf.street: 
                    hole.traffic_count += (traf.total_passing_volume)/2
                else:
                    hole.traffic_count += SIDE_TRAFFIC *(traf.total_passing_volume)/2
    return pothole

def Status(pothole_list_objects):
    '''
    Ranks the potholes from 1 to 5 with 5 being the most
    important pothole and 1 being the least important 
    pothole. Rankings are based on the relative traffic
    among potholes

    Inputs: 
        pothole_list_objects: list of potholes

    Returns:
        list of potholes with modified status
    '''
    broken_list =[]
    sorted_list = sorted(pothole_list_objects, key=lambda pothole: pothole.traffic_count)
    length = len(sorted_list)//31
    for i in range(31):
        broken_list.append(sorted_list[i*length:(i+1)*length])
    very_high = broken_list[0]
    high = broken_list[1]+ broken_list[2]
    medium =[]
    for i in range(3,7):
        medium += broken_list[i]
    low = []
    for i in range(7,15):
        low += broken_list[i]
    very_low =[]
    for i in range(15,31):
        very_low += broken_list[i]
    urgency_levels = [very_high, high, medium, low, very_low]
    urgency_names = ['Very High', 'High', 'Medium', 'Low', 'Very Low']
    for level, urgency in enumerate(urgency_levels):
        for pothole in urgency:
            level_name = urgency_names[level]
            pothole.urgency_level = level_name
    return urgency_levels

def Update_Potholes(pothole_list_objects, db):
    '''
    Updates the potholes in the databse

    Inputs:
        pothole_list_objects: modified list of pothole objects
        db: database name
    '''
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    count = 0
    total = len(pothole_list_objects)
    for pothole in pothole_list_objects:
        count += 1
        if count%100 == 0:
            print("       ",count, " out of " , total, "potholes updated")
        query="""UPDATE potholes SET traffic = ?, urgency = ? 
                WHERE service_request_number = ?"""
        args = (pothole.traffic_count, pothole.urgency_level, pothole.service_num)  
        cur.execute(query, args)
    conn.commit()
    conn.close()




### Direct Copy -dict factory ####
### From: http://stackoverflow.com/questions/811548
###     /sqlite-and-python-return-a-dictionary-using-fetchone
def dict_factory(cursor, row):
    '''
    Creates a dictionary
    '''
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def main(query, db, args):
    '''
    Takes a query to create potholes, a database and a set of arguments
    Returns a JSON file
    '''
    x = create_query_dict(query, db, args)
    l = create_pothole(x)

    rv = []
    for pothole in l:
        rv.append(eval(json.dumps(pothole.__dict__)))
    return rv


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python3 {} <database filename>".format(sys.argv[0]))
        sys.exit(1)

    go(sys.argv[1])