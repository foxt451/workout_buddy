import random
from django import template
from django.contrib.gis.geos import Point, GEOSGeometry

sport_icons = [
    'fa-weight-hanging',
    'fa-person-running',
    'fa-baseball-bat-ball',
    'fa-broom-ball',
    'fa-dumbbell',
    'fa-bowling-ball',
    'fa-hockey-puck',
    'fa-medal',
    'fa-volleyball',
    'fa-basketball',
    'fa-futbol',
    'fa-person-biking',
    'fa-heart-pulse',
    'fa-stopwatch-20',
]

register = template.Library()

@register.simple_tag
def random_sport_icon():
    return random.choice(sport_icons)

@register.filter
def to_geom(point):
    return GEOSGeometry(point)

import geopy.distance
@register.simple_tag
def distance(pointA, pointB):
    print(pointA, pointB)
    dist = geopy.distance.distance(geopy.distance.lonlat(*pointA.tuple), geopy.distance.lonlat(*pointB.tuple)).km
    return dist