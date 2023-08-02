from django.shortcuts import render, HttpResponseRedirect, redirect
from markdown2 import Markdown
from django.urls import reverse
from . import util
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def greet(request, title):
    markdowner = Markdown()
    titles = util.get_entry(title)
    if titles == None:
        return render(request, "encyclopedia/pagenotfound.html", {
            "page": title
        })
    else:
        return render(request, "encyclopedia/get_entry.html", {
            "loop": markdowner.convert(titles),
            "page": title
        })


def search(request):
    markdowner = Markdown()
    message = request.GET.get('q')
    rp = util.get_entry(message)
    present = util.list_entries()
    wilco = []
    if rp == None:
        for i in present:
            if message.upper() in i.upper():
                wilco.append(i)
        return render(request, "encyclopedia/search.html", {
            "wilco": wilco,
            "page": message
        })
    else:
        return render(request, "encyclopedia/get_entry.html", {
            "loop": markdowner.convert(rp),
            "page": message
        })


def create(request):
    if request.method == "POST":
        filename = request.POST.get('title')
        contents = request.POST.get('content')
        if filename in util.list_entries():
            return render(request, "encyclopedia/error.html")
        util.save_entry(filename, contents)
        return redirect("greet", title=filename)
    return render(request, "encyclopedia/newpage.html")


def randompage(request):
    ppl = random.choice(util.list_entries())
    return redirect("greet", title=ppl)


def edit(request, title):
    print("0", title)
    contents = util.get_entry(title)
    if request.method == "POST":
        print("1", contents)
        contents = request.POST.get('content')
        print("2", contents)
        util.edit_page(title, contents)
        return redirect("greet", title=title)
    return render(request, "encyclopedia/edit.html", {
        'body': contents,
        'title': title
    })
