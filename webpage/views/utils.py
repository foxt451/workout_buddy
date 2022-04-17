from ipware import get_client_ip
from django.contrib.gis.geoip2 import GeoIP2

# throws error
def get_user_coords(request):
    client_ip, is_routable = get_client_ip(request)
    client_ip = '176.36.32.100'
    g = GeoIP2()
    return g.lat_lon(client_ip)
