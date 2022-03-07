from django.contrib.gis.geoip2 import GeoIP2


def get_location(ip):
    geoip = GeoIP2()

    return geoip.city(ip)

def get_center_coords(location_lat, location_lng, destination_lat = None, destination_lng = None):
    coords = (location_lat, location_lng)

    if destination_lat and destination_lng:
        coords = [(location_lat + destination_lat) / 2, (location_lng + destination_lng) / 2]

    return coords

def get_zoom(distance):
    if distance <= 100 :
        return 8
    elif distance > 100 and distance <= 500:
        return 6
    else:
        return 4