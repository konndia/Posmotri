const container = document.querySelector(".container");
const count = document.getElementById("count");
const seat_sel = document.getElementById("id_seat");
const amount = document.getElementById("amount");
const select = document.getElementById("movie");
const seats = document.querySelectorAll(".seat:not(.reserved)");


getFromLocalStorage();
// calculateTotal();

container.addEventListener("click", function(e){
    if(e.target.classList.contains('seat') && !e.target.classList.contains('reserved') ) {
        e.target.classList.toggle("selected");
        calculateTotal();  
    }
});

select.addEventListener("change", function (e) { 
    calculateTotal();
    showBooks();
 });

 function showBooks() {
    document.getElementById("aaaa").innerHTML = select.options[select.selectedIndex].text;
    const allSeats = container.querySelectorAll('.seat');
    const seatsBooked = document.getElementsByClassName(select.options[select.selectedIndex].text);
    const seatsBooked1 = [];
    const seatsBooked2 = [];
    const seatsBooked3 = [];

    for (let item of seatsBooked) {
        seatsBooked1.push(item.innerHTML)
    }
    
    console.log(seatsBooked1)
    for (let item of seatsBooked1) {
        seatsBooked2.push(item.split(','))
    }
    console.log(seatsBooked2)
    for (let item of seatsBooked2) {
        seatsBooked3.push(...item)
    }
    console.log(seatsBooked3)

    allSeats.forEach(function(seat) {
        seat.className = "seat"
        if (seatsBooked3.includes(seat.innerHTML)) {
            seat.className = "seat reserved";
        }
    });
}

function calculateTotal() {
    const selectedSeats = container.querySelectorAll('.seat.selected');

    const selectedSeatsArr = [];
    const seatsArr=[];
    const selectedSeatsArrId = [];

    selectedSeats.forEach(function(seat) {
        selectedSeatsArr.push(seat);
        selectedSeatsArrId.push(seat.innerHTML);
    });

    seats.forEach(function(seat) {
        seatsArr.push(seat);
    });

    let selectedSeatIndexs = selectedSeatsArr.map(function(seat) {
        return seatsArr.indexOf(seat);
    });

    let selectedSeatCount = selectedSeats.length;
    count.innerText = selectedSeatCount;
    amount.innerText = selectedSeatCount*select.value;
    seat_sel.value = selectedSeatsArrId;

    saveToLocalStorage(selectedSeatIndexs); 
    }

 function getFromLocalStorage() { 
    const selectedSeats =JSON.parse(localStorage.getItem('selectedSeats'));

    if (selectedSeats != null && selectedSeats.length > 0) {
        seats.forEach(function(seat, index) {
            if (selectedSeats.indexOf(index) > -1) {
                seat.classList.add("selected");
            }
        });
    }

    const selectedMovieIndex = localStorage.getItem('selectedMovieIndex');

    if (selectedMovieIndex != null) {
        select.selectedIndex = selectedMovieIndex;
    }
  }

 function saveToLocalStorage(indexs) {
     localStorage.setItem('selectedSeats', JSON.stringify(indexs));
     localStorage.setItem('selectedMovieIndex', select.selectedIndex);
 }