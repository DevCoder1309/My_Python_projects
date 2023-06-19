from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse
# Create your views here.


class NewTaskForm(forms.Form):
    task = forms.CharField(
        label="New task", widget=forms.TextInput(attrs={'size': '50'}))
    due_date = forms.CharField(
        label="Due date", widget=forms.TextInput(attrs={'size': '50'}))
    status = forms.CharField(
        label="Status", widget=forms.TextInput(attrs={'size': '50'}))


def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
        request.session["due_dates"] = []
        request.session["statuses"] = []
    content = zip(
        request.session["tasks"], request.session["due_dates"], request.session["statuses"])
    return render(request, "tasks/index.html", {
        "content": content
    })


def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            due_date = form.cleaned_data["due_date"]
            status = form.cleaned_data["status"]
            request.session["tasks"] += [task]
            request.session["due_dates"] += [due_date]
            request.session["statuses"] += [status]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return (request, "tasks/add.html", {
                "form": form
            })
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })


def remove(request):
    request.session["tasks"] = []
    request.session["due_dates"] = []
    request.session["statuses"] = []
    return HttpResponseRedirect(reverse("tasks:index"))
