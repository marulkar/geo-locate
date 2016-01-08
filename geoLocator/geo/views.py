from django.shortcuts import render
from geoLocator.settings import GOOGLE_API_KEY
import requests
import json
# Create your views here.
def geo(request):

    return render(request, 'geo/geo.html', {"api":GOOGLE_API_KEY}) 
