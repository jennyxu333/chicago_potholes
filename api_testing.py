import csv

ph = open('potholes_reported.csv', 'r')
fieldnames = ('creation_date', 'status', 'completion_date', 'service_request_number',\
                'type_of_service_request', 'current_activity', 'most_recent_action', \
                'number_of_potholes_filled_on_block', 'street_address', 'zip', \
                'x_coordinate', 'y_coordinate', 'ward', 'police_district', \
                'community_area', 'ssa', 'latitude', 'longtitude', 'location', \
                'location_zip', 'location_city', 'location_address', 'location_state')
reader = csv.DictReader(ph, fieldnames)
