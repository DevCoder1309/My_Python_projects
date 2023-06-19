from django.shortcuts import render
import datetime
now = datetime.datetime.now()
# Create your views here.
def ankit(request):
    return render(request, "newyear/ankit.html",{
        "isitnewyear": isitnewyear()
    })
def isitnewyear():
    if now.month!=1 and now.day!=1:
        return False
    else:
        return True