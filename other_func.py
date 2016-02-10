import sys
sys.path.append("/usr/local/lib/python2.7/dist-packages")
import geopy

from geopy.distance import vincenty
newport_ri = (41.49008, -71.312796)
cleveland_oh = (41.499498, -81.695391)
print(vincenty(newport_ri, cleveland_oh).miles)


def distance_between_traffic_pothole(tlat, tlon, plat, plon):
    pothole = (plat, plon)
    traffic = (tlat, tlon)
    miles = vincenty(pothole, traffic).miles
    return miles

def download_csv():
    import requests
    link = "https://data.cityofchicago.org/api/views/7as2-ds3y/rows.csv?accessType=DOWNLOAD"
    r = requests.get(link)
    return r

def 