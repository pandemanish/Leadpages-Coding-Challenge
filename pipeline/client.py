import requests
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type
from pipeline.logger import Logger
from config import BASE_URL, STOP_AFTER_ATTEMPT, WAIT_FIXED

logger = Logger()

class Client:
    
    def __init__(self, headers):
        self.headers = headers
    
    def retry_error_callback(retry_state):
        logger.error(f"Request failed with status code {retry_state.outcome.exception()}")

    @retry(stop=stop_after_attempt(STOP_AFTER_ATTEMPT),
           wait=wait_fixed(WAIT_FIXED),
           retry=retry_if_exception_type(requests.exceptions.RequestException),
           retry_error_callback=retry_error_callback
        )
    def fetch_animals_list(self, page):
        url = f"{BASE_URL}/animals?page={page}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    

    @retry(stop=stop_after_attempt(STOP_AFTER_ATTEMPT),
           wait=wait_fixed(WAIT_FIXED),
           retry=retry_if_exception_type(requests.exceptions.RequestException),
           retry_error_callback=retry_error_callback
        )
    def fetch_animal_details(self, animal_id):
        
        url = f"{BASE_URL}/animals/{animal_id}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    @retry(stop=stop_after_attempt(STOP_AFTER_ATTEMPT),
           wait=wait_fixed(WAIT_FIXED),
           retry=retry_if_exception_type(requests.exceptions.RequestException),
           retry_error_callback=retry_error_callback
    )
    def post_batch(self, animals):
        url = f"{BASE_URL}/home"
        response = requests.post(url, headers=self.headers, json=animals)
        response.raise_for_status()
        return response.json()

