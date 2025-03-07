from django.shortcuts import render

from services import drivers_service



# Create your views here.
def driver_list(request):
    drivers = drivers_service.get_drivers()
    return render(request, 'driver_list.html', {'drivers': drivers})

def driver_detail(request, driverId):
    driver = drivers_service.get_driver(driverId)
    return render(request, 'driver_detail.html', {"driver": driver})
