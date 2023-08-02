from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render
from django.urls import reverse
from .models import User, Active_Listening, Category, Bid, Comment
from django import forms
from django.forms import ModelForm
from django import forms

class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']
    def __init__(self, *args, **kwargs):
        super(BidForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control m-2'
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
    widgets = {
        "comment": forms.CharField(
            label="Comment", widget=forms.TextInput(attrs={'size': '50'}))
    }
def index(request):
    data = Active_Listening.objects.all()
    return render(request, "auctions/index.html", {
        "datas": data,
        "title": "Active Listings",
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def active_listening(request,id):
    active_listening = Active_Listening.objects.get(pk=id)
    bid_amount = Bid.objects.filter(auction=active_listening)
    comments = Comment.objects.filter(auction=id)
    if active_listening.closed:
        ended = True
        return render(request, "auctions/winner.html", {
            "ended": ended,
            "context": bid_amount,
            "comment_form": CommentForm(),
            "comments": comments,
        })
    return render(request, "auctions/active_listening.html", {
        "active_listening": active_listening,
        "bid_form": BidForm(),
        "bid_amount": bid_amount
    })


def categories_list(request):
    return render(request, "auctions/category_list.html", {
        "categories": Category.objects.all()
    })

def create(request):
    class NewTaskForm(ModelForm):
        photo_url = forms.CharField(
            label="Photo URL", widget=forms.TextInput(attrs={'size': '50'}))
        item = forms.CharField(
            label="Title", widget=forms.TextInput(attrs={'size': '50'}))
        description = forms.CharField(
            label="Description", widget=forms.TextInput(attrs={'size': '50'}))
        currentprice = forms.IntegerField(
            label="Current Price", widget=forms.TextInput(attrs={'size': '50'}))
        class Meta:
            model = Active_Listening
            fields = ['photo_url', 'item', 'description', 'currentprice']
    form = NewTaskForm(request.POST)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'auctions/create.html', {
        'forms': form
    })

def add_watchlist(request,id):
    data = Active_Listening.objects.get(pk=id)
    watchlist = request.user.watchlist
    if data in watchlist.all():
        watchlist.remove(data)
    else:
        watchlist.add(data)
    return HttpResponseRedirect(reverse('watchlist'))
def Watchlist(request):
    return render(request, "auctions/watchlist.html",{
        "datas": request.user.watchlist.all()
    })


def category(request, name):
    category = Category.objects.get(name=name)
    auctions = Active_Listening.objects.filter(
        category=category,
    )
    return render(request, "auctions/index.html", {
        "datas": auctions,
        "title": category.name
    })


def categories_list(request):
    return render(request, "auctions/category_list.html", {
        "categories": Category.objects.all()
    })

def Biding(request, id):
    if request.method=="POST":
        bid_form = BidForm(request.POST or None)
        if bid_form.is_valid():
            auction = Active_Listening.objects.get(id=id)
            user = request.user
            new_bid = bid_form.save(commit=False)
            current_bids = Bid.objects.filter(auction=auction)
            is_highest_bid = all(new_bid.amount > n.amount for n in current_bids)
            is_valid_first_bid = new_bid.amount >= auction.price 
            if is_highest_bid and is_valid_first_bid:
                new_bid.auction = auction
                new_bid.user = request.user
                new_bid.save()
            else:
                return render(request, "auctions/error.html")
    return HttpResponseRedirect(reverse('active_listening', kwargs={'id': id}))


def auction_close(request, id):
    auction = Active_Listening.objects.get(id=id)
    winner = Bid.objects.filter(auction=auction)
    auction.closed =  True
    auction.save()
    return render(request, "auctions/winner.html",{
        "context": winner
    })

def comment(request, id):
    auction = Active_Listening.objects.get(pk=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data["comment"]
            comment = Comment(
                user=User.objects.get(pk=request.user.id),
                comment=comment,
                auction=auction
            )
            comment.save()
        url = reverse('active_listening', kwargs={'id': id})
        return HttpResponseRedirect(url)
