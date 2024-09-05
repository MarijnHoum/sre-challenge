# A client simulation script

import logging
import random
import time

import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_URL = "http://localhost:8000"

timeout = 5
sleep_min = 0.05
sleep_max = 1
error_404_p = 1/10
error_422_p = 1/10

def make_request(session, method, url, **kwargs):
    result = getattr(session, method)(url, **kwargs)
    logger.info("%s %s %s", method, url, result)

def simulate_traffic():
    session = requests.Session()
    while True:
        if random.random() < error_404_p:
            make_request(session,"get", f"{BASE_URL}/does_not_exist", timeout=timeout)
        else:
            make_request(session,"get", f"{BASE_URL}/properties", timeout=timeout)
        if random.random() < error_422_p:
            make_request(session, "post", f"{BASE_URL}/inquiries", data="} Invalid JSON {", timeout=timeout)
        else:
            make_request(session,"post", f"{BASE_URL}/inquiries", json={"inquiry": "Example Inquiry"},
                         timeout=timeout)
        time.sleep(random.uniform(sleep_min, sleep_max))  # Random traffic spikes

if __name__ == "__main__":
    simulate_traffic()
