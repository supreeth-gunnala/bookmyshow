let selectedSeats = [];

function toggleSeat(seat) {
    const btn = document.getElementById(seat);

    if (btn.classList.contains("selected")) {
        btn.classList.remove("selected");
        btn.classList.add("available");
        selectedSeats = selectedSeats.filter(s => s !== seat);
    } else {
        btn.classList.remove("available");
        btn.classList.add("selected");
        selectedSeats.push(seat);
    }

    document.getElementById("seatsInput").value = selectedSeats.join(",");
}
