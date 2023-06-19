from django.urls import path
from . import views
urlpatterns = [
    path("isitnewyear", views.ankit, name="index")
]