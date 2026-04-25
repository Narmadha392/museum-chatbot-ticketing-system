from fastapi import FastAPI
import random

app = FastAPI()

ADULT_PRICE = 200
KID_PRICE = 100

@app.get("/")
def home():
    return {"message": "Backend running"}

@app.post("/book_ticket")
def book_ticket(adults: int, kids: int):
    total = (adults * ADULT_PRICE) + (kids * KID_PRICE)
    ticket_id = "T" + str(random.randint(10000, 99999))

    return {
        "ticket_id": ticket_id,
        "total_price": total,
        "status": "Payment Successful (Mock)"
    }