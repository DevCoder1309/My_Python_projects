from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.greet, name="greet"),
    path('search', views.search, name="search"),
    path('create',views.create, name="create"),
    path('randompage', views.randompage, name="randompage"),
    path('edit/<str:title>', views.edit, name="edit")
]
