from potholes_site.update import *
import statistics as stat
import datetime
import json 

def stat_dict(wards, db):
    '''
    Creates a list of JSON dictionaries representing wards

    Inputs:
        wards: list of wards
        db: database name

    Returns:
        json_list: list of JSON dictionaries 
    '''
    ward_list = []
    for ward in wards:
        ward_obj = StatWard(ward, db)
        ward_list.append(ward_obj)

    json_list= [] 
    for ward in ward_list:
        json_list.append(eval(json.dumps(ward.__dict__)))
    return json_list
    

class StatWard(object):
    def __init__(self, ward, db):
        '''
        Creates an object represnting a ward and 
        various statistics
        '''
        self.ward = ward
        self.db = db
        l = self.create_potholes_for_ward()
        self.open_potholes = self.open_potholes(l)
        self.average, self.max_time, self.median = self.response_time(l)
        self.traffic_in_ward = self.traffic_in_ward(l)

    def create_potholes_for_ward(self):
        '''
        Creates a list of potholes in the ward
        '''
        query = '''SELECT * FROM potholes WHERE ward == ? '''
        arg = (str(self.ward), )
        query_dict = create_query_dict(query, self.db, arg)
        l = create_pothole(query_dict)
        return l

    def open_potholes(self, pothole_list):
        '''
        Counts the number of open potholes in the ward

        Input:
            pothole_list: list of pothole objects

        Returns: 
            count: number of open potholes
        '''
        count = 0
        for pothole in pothole_list:
            if pothole.status == "Open":
                count += 1
        return count

    def response_time(self, pothole_list):
        '''
        Counts the number of open potholes in the ward

        Input:
            pothole_list: list of pothole objects

        Returns: 
            tuple: (average reponse time, max reponse time,
                    median reponse time)
        '''
        count = 0
        response = 0
        max_time = []
        for pothole in pothole_list:
            if pothole.status == "Completed":
                response += int(pothole.response_time)
                count += 1
                max_time.append(int(pothole.response_time))
        if count == 0:
            average = 0
            max_time = [0]
        else:
            average = round(response/count)
        return (average, max(max_time), stat.median(max_time))

    def traffic_in_ward(self, pothole_list):
        '''
        Finds the trafic count in the ward

        Input:
            pothole_list: list of pothole objects

        Returns: 
           traf: count of traffic
        '''
        traf = 0
        for pothole in pothole_list:
            traf += pothole.traffic_count
        return traf 

