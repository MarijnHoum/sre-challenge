## A flaky web APP

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random
import time

delay_min = 0.1
delay_max = 2.0
error_500_p = 1/10

app = FastAPI()

# Define the data model for inquiries
class Inquiry(BaseModel):
    inquiry: str

# Simulate property listings
properties = [
    {"id": 1, "name": "Oceanview Apartment", "price": 300000},
    {"id": 2, "name": "Downtown Loft", "price": 450000},
    {"id": 3, "name": "Suburban House", "price": 600000},
]

# Helper function to simulate random delays and random errors
def simulate_random_delay_and_error():
    # Random delay between 100ms and 2000ms
    delay = random.uniform(delay_min, delay_max)
    time.sleep(delay)

    # 20% chance of returning a 500 error
    if random.random() < error_500_p:
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Endpoint to get property listings
@app.get("/properties")
async def get_properties():
    simulate_random_delay_and_error()
    return {"properties": properties}

# Endpoint to submit an inquiry
@app.post("/inquiries")
async def submit_inquiry(inquiry: Inquiry):
    simulate_random_delay_and_error()
    return {"message": "Inquiry received", "inquiry": inquiry.inquiry}
