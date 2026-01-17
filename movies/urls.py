from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("", views.home, name="home"),
    path("movie/<int:movie_id>/", views.movie_detail, name="movie_detail"),
    path("movie/<int:movie_id>/book/", views.book_tickets, name="book_tickets"),
    path("booking-success/<int:booking_id>/", views.booking_success, name="booking_success"),
]
