from django.http import response
import requests 
from django.shortcuts import render, get_list_or_404

from models import Driver


API_URL = "https://f1api.dev/api/drivers"

def get_drivers():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    return []

def get_driver(driverId):
    response = requests.get(f"{API_URL}/{driverId}")
    if response.status_code == 200:
        return response.json()
    return []

def load_drivers():
    if not Driver.objects.count():
        drivers = get_drivers()
        for driver in drivers:
            Driver.objects.create(
                name=driver["name"],
                surname=driver["surname"],
                nationality=driver["nationality"],
                birthday=driver["birthday"],
                url=driver["url"],
            )
        return f"{len(drivers)} conductores cargados"
    return "Los productos ya estan en la base de datos"
