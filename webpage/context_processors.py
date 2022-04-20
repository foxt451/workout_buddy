from django.conf import settings


def google_api_key(request):
    return {'google_api': settings.GOOGLE_MAPS_API_KEY}