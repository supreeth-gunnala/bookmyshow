from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import SignupForm
from movies.models import Booking


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created. Please login.")
            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'users/signup.html', {'form': form})


@login_required
def profile(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'users/profile.html', {'bookings': bookings})
