from django.contrib import admin
from .models import Airport, Flight, Passenger
# Register your models here.
class Flight_set(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")
class Passenger_set(admin.ModelAdmin):
    filter_horizontal = ("flights",)
admin.site.register(Airport)
admin.site.register(Flight, Flight_set)
admin.site.register(Passenger, Passenger_set)