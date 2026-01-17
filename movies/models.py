from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=150.00)
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)
    description = models.TextField(blank=True)
    trailer_url = models.URLField(blank=True, null=True)

    genre = models.ManyToManyField(Genre, blank=True)
    language = models.ManyToManyField(Language, blank=True)

    def __str__(self):
        return self.title

    def get_embed_url(self):
        if not self.trailer_url:
            return ""
        if "watch?v=" in self.trailer_url:
            return self.trailer_url.replace("watch?v=", "embed/")
        if "youtu.be/" in self.trailer_url:
            video_id = self.trailer_url.split("/")[-1]
            return f"https://www.youtube.com/embed/{video_id}"
        return self.trailer_url



class Booking(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seats = models.JSONField(default=list)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie} - {self.user}"
