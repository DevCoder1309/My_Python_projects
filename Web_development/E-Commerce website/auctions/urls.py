from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("active_listening/<int:id>", views.active_listening, name="active_listening"),
    path("create", views.create, name="create"),
    path("Watchlist/<int:id>", views.add_watchlist, name="add_watchlist"),
    path("Watchlist", views.Watchlist, name="watchlist"),
    path("categories", views.categories_list, name="categories"),
    path("categories/<str:name>", views.category, name="category"),
    path("auction/<int:id>/bid", views.Biding, name="Biding"),
    path("auction/<int:id>/close", views.auction_close, name="close_auction"),
    path("auction/<int:id>/comment", views.comment, name="comment"),
]
