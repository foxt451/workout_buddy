from ipware import get_client_ip
from django.contrib.gis.geoip2 import GeoIP2
from django.contrib.gis.geoip2 import geoip2
from django.contrib.gis.forms.widgets import OSMWidget
# from leaflet.forms.widgets import LeafletWidget

# throws error


def get_user_coords(request):
    client_ip, is_routable = get_client_ip(request)
    client_ip = '176.36.32.100'
    g = GeoIP2()
    return g.lat_lon(client_ip)


def set_form_field_widget_to_osmw_with_default_location(request, form, field_name):
    try:
        (lat, lon) = get_user_coords(request)
        osmw = OSMWidget(
            attrs={'default_lat': lat, 'default_lon': lon, 'geom_type': 'POINT'})
    except geoip2.errors.AddressNotFoundError:
        osmw = OSMWidget(attrs={'geom_type': 'POINT'})
    form.fields[field_name].widget = osmw

# LEAFLET_WIDGET_ATTRS = {
#     'geom_type': 'Point',
# }
    
# def set_form_field_widget_to_leaflet_with_default_location(request, form, field_name):
#     try:
#         (lat, lon) = get_user_coords(request)
#         leaflet = LeafletWidget(attrs={**LEAFLET_WIDGET_ATTRS, 'settings_overrides': {
#                 'DEFAULT_CENTER': (lat, lon),
#                 'DEFAULT_ZOOM': 10
#             }}
#             )
#     except geoip2.errors.AddressNotFoundError:
#         leaflet = LeafletWidget(attrs=LEAFLET_WIDGET_ATTRS)
#     print(leaflet)
#     form.fields[field_name].widget = leaflet
    
# def set_form_field_widget_to_google_with_default_location(request, form, field_name):
#     try:
#         (lat, lon) = get_user_coords(request)
#         leaflet = LeafletWidget(attrs={**LEAFLET_WIDGET_ATTRS, 'settings_overrides': {
#                 'DEFAULT_CENTER': (lat, lon),
#                 'DEFAULT_ZOOM': 10
#             }}
#             )
#     except geoip2.errors.AddressNotFoundError:
#         leaflet = LeafletWidget(attrs=LEAFLET_WIDGET_ATTRS)
#     print(leaflet)
#     form.fields[field_name].widget = leaflet
