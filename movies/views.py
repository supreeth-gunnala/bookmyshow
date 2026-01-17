from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Movie, Booking


def home(request):
    movies = Movie.objects.all()
    return render(request, "movies/home.html", {"movies": movies})


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, "movies/movie_detail.html", {"movie": movie})


@login_required
def book_tickets(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    rows = ["A","B","C","D","E","F","G","H","I","J"]
    cols = range(1, 11)

    booked_seats = set()
    for booking in Booking.objects.filter(movie=movie):
        booked_seats.update(booking.seats)

    seat_layout = []
    for r in rows:
        row = []
        for c in cols:
            seat = f"{r}{c}"
            row.append({
                "name": seat,
                "occupied": seat in booked_seats
            })
        seat_layout.append(row)

    if request.method == "POST":
        seats_raw = request.POST.get("seats", "")
        selected_seats = [s for s in seats_raw.split(",") if s]

        if not selected_seats:
            messages.error(request, "Please select at least one seat")
            return redirect("movies:book_tickets", movie_id=movie.id)

        if set(selected_seats) & booked_seats:
            messages.error(request, "Some seats are already booked")
            return redirect("movies:book_tickets", movie_id=movie.id)

        booking = Booking.objects.create(
            movie=movie,
            user=request.user,
            seats=selected_seats,
            total_price=len(selected_seats) * movie.price
        )

        # ✅ CORRECT REDIRECT
        return redirect("movies:booking_success", booking_id=booking.id)

    return render(request, "movies/book_tickets.html", {
        "movie": movie,
        "seat_layout": seat_layout,
        "seat_price": movie.price
    })


@login_required
def booking_success(request, booking_id):
    booking = get_object_or_404(
        Booking,
        id=booking_id,
        user=request.user
    )
    return render(request, "movies/booking_success.html", {
        "booking": booking
    })
