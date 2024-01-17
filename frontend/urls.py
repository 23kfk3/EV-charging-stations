from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page),
    path('navigation', navigation_page),
    path('service', service_page),
    path('contact', contact_page),
    path('station', station_page),
    path('login', login_page)
]