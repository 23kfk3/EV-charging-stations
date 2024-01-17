from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'index.html')

def navigation_page(request):
    return render(request, 'navigation.html')

def service_page(request):
    return render(request, 'service.html')

def login_page(request):
    return render(request, 'login.html')

def contact_page(request):
    return render(request, 'contact.html')

def station_page(request):
    return render(request, 'station.html')