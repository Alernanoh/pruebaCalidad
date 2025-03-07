from django.http import response
import requests 
from django.shortcuts import render, get_list_or_404


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


