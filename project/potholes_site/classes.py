import sqlite3
import json
import math


class Pothole(object):

    def __init__(self, creation_date, status, completion_date, response_time,\
                 service_num, current_activity, action, potholexblock, \
                 street, zip_num, ward, lat, lon, urgency_level, \
                 traffic_count, street_only):
        '''
        Creates an object representing a single pothole
        '''
        self.creation_date = creation_date
        self.status = status
        self.completion_date = completion_date
        self.response_time = response_time
        self.service_num = service_num
        self.current_activity = current_activity
        self.action = action
        self.potholexblock = potholexblock
        self.street = street
        self.street_only = street_only
        self.zip = zip_num
        self.ward = ward
        self.lat = lat
        self.lon = lon
        self.urgency_level = urgency_level
        self.traffic_count = traffic_count
        self.begin =int(creation_date[8:])
        if self.completion_date != "":
            self.end = int(completion_date[8:])
        else:
            self.end = 32

    def distance_traffic(self, tlat, tlon):
        '''
        Finds the distance between the traffic object and 
        pothole object

        Inputs:
            tlat: latitude of traffic object
            tlon: longitude of traffic object

        Returns:
            miles: distance in miles
        
        Source: http://gis.stackexchange.com/a/56589/15183
        Direct Copy
        '''
        # convert decimal degrees to radians 
        lon1, lat1, lon2, lat2 = map(math.radians, [self.lon, self.lat, tlon, tlat])
        # haversine formula 
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a)) 
        miles = 6367 * c*0.62137119
        return miles
    

    def __repr__(self):
        return self.service_num

class Traffic(object):

    def __init__(self, ID,count_location,street , \
        total_passing_volume , volume_by_direction , \
        latitude ,longitude):
        '''
        Creates an object representing a single traffic point
        '''
        self.id = int(ID)
        self.count_location = count_location
        self.total_passing_volume = int(total_passing_volume)
        self.volume_by_direction = volume_by_direction
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.street = street

    def __repr__(self):
        return "The traffic on "+ self.count_location+ " " +\
            self.street

class Alderman(object):

    def __init__(self, name, email, ward):
        self.email_address = str(email)
        self.name = name
        self.ward = ward


    def email(self, message):
        '''
        Sends an email message to the Alderman

        Inputs:
            message: message of the email

        '''
        #### Direct Copy From Automate the Boring Stuff ####
        ##### https://automatetheboringstuff.com/chapter16/ ###
        
        import smtplib

        sender = 'chicagopothole@yahoo.com'
        receivers = self.email_address

        smtpObj = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login('chicagopothole@yahoo.com', \
                    'shutyourpothole')
        x = smtpObj.sendmail(sender,receivers,message)
        smtpObj.quit()

    def __repr__(self):
        return "Alderman " + self.name


    