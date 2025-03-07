from django.urls import path
from .views import driver_list, driver_detail
from . import views

urlpatterns = [
    path("", views.driver_list, name="driver_list"),
    path("driver/<int:id>", views.driver_detail, name="driver_detail"),
]
