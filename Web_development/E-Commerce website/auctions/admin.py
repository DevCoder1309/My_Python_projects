from django.contrib import admin
from .models import User, Active_Listening, Category, Bid, Comment
# Register your models here.


class Flight_set(admin.ModelAdmin):
    list_display = ("id","photo_url", "item", "description", "price")
admin.site.register(User)
admin.site.register(Active_Listening, Flight_set)
admin.site.register(Category)
admin.site.register(Bid)
admin.site.register(Comment)