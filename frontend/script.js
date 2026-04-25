async function bookTicket() {
    let adults = document.getElementById("adults").value;
    let kids = document.getElementById("kids").value;

    let response = await fetch(
        `http://127.0.0.1:8000/book_ticket?adults=${adults}&kids=${kids}`,
        {
            method: "POST"
        }
    );

    let data = await response.json();

    document.getElementById("result").innerText =
        "✅ Ticket ID: " + data.ticket_id +
        " | Total Price: ₹" + data.total_price;
}
