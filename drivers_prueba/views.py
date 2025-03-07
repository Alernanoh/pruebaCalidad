from django.shortcuts import render

from drivers_prueba.services.drivers_service import get_drivers, get_driver


# Create your views here.
def driver_list(request):
    drivers = get_drivers()
    return render(request, 'driver_list.html', {'drivers': drivers})

def driver_detail(request, id):
    driver = get_driver(id)
    return render(request, 'driver_detail.html', {"driver": driver})
