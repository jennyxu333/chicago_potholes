class Alderman(object):

    def __init__(self, name, ward, email):
        self.email_address = email
        self.name = name
        self.ward = ward


    def email(self, message):
        import smtplib

        sender = 'chicagopothole@yahoo.com'
        receivers = [self.email_address]

        smtpObj = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login('chicagopothole@yahoo.com', 'shutyourpothole')
        x = smtpObj.sendmail(sender,receivers,message)
        smtpObj.quit()

    def __repr__(self):
        return "Alderman " + self.name




class Pothole(object):

    def __init__(self, creation_year, creation_month, creation_day, status, \
                 completion_year, completion_month, completion_day, \
                 service_num, current_activity, action, potholexblock, \
                 street, zip_num, ward, community, lat, lon):
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.creation_day = creation_day
        self.status = status
        self.completion_year = completion_year
        self.completion_month = completion_month
        self.completion_day = completion_day
        self.service_num = service_num
        self.current_activity = current_activity
        self.action = action
        self.potholexblock = potholexblock
        self.street = street
        self.zip = zip_num
        self.ward = ward
        self.community = community
        self.lat = lat
        self.lon = lon
        import sys
        sys.path.append("/usr/local/lib/python2.7/dist-packages")
        import geopy
        from geopy.distance import vincenty

    def distance_between_traffic_pothole(tlat, tlon):
        pothole = (self.lat, self.lon)
        traffic = (tlat, tlon)
        miles = vincenty(pothole, traffic).miles
        return miles




class Traffic(object):

    def __init__(self, ID,count_location,street , \
        total_passing_volume , volume_by_direction , \
        latitude ,longitude):
        self.id = int(ID)
        self.count_location = count_location
        self.total_passing_volume = int(total_passing_volume)
        self.volume_by_direction = volume_by_direction
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.street = street


