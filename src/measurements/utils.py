from django.contrib.gis.geoip2 import GeoIP2


def get_location(ip):
    geoip = GeoIP2()

    return geoip.city(ip)
