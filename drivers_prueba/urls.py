from django.urls import path
from . import views

urlpatterns = [
    path(" ", views.driver_list, name="driver_list"),
    path("driver/<int:id>", views.driver_detail, name="driver_detail"),
]
