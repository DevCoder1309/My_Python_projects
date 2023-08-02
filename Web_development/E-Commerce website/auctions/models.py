from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):
    pass
class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name}"

    @property
    def count_active_auctions(self):
        return Active_Listening.objects.filter(category=self).count()
class Active_Listening(models.Model):
    photo_url = models.CharField(
        max_length=200)
    item = models.CharField(max_length=64)
    price = models.IntegerField(default=123)
    description = models.CharField(max_length=200, default='Basketball')
    category = models.ForeignKey(
        Category,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="auctions"
    )
    watchlist = models.ManyToManyField(
        User,
        blank=True,
        related_name="watchlist"
    )
    closed = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.photo_url} {self.item} {self.description}"
class Bid(models.Model):
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bids")
    auction = models.ForeignKey(
        Active_Listening, on_delete=models.CASCADE, related_name="bids")

    def __str__(self):
        return f"Bid #{self.id}: {self.amount} on {self.auction.item} by {self.user.username}"
    

class Comment(models.Model):
    comment = models.TextField(blank=False)
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments")
    auction = models.ForeignKey(
        Active_Listening, on_delete=models.CASCADE, related_name="comments")

    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"

    def __str__(self):
        return f"Comment #{self.id}: {self.user.username} on {self.auction.item}: {self.comment}"
