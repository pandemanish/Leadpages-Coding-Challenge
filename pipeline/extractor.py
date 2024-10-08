
from pipeline.client import Client
from config import BATCH_SIZE


class Extractor:
    client: Client = None
    current_page:int = 1
    total_pages:int = None
    queue = []
    
    def __init__(self, client: Client):
        self.client = client
    
    def fetch_animals_list(self, page):
        response_json = self.client.fetch_animals_list(page)
        self.total_pages = response_json['total_pages']
        return response_json['items']
    
    def fetch_animal_details(self, animal_id):
        return self.client.fetch_animal_details(animal_id)


    def get_next_animals_batch(self):
        animal_details = []
        while len(animal_details) < BATCH_SIZE and (self.queue or (not self.total_pages) or (self.current_page <= self.total_pages)):
            if not self.queue:
                self.queue = self.fetch_animals_list(self.current_page)
                self.current_page += 1

            while self.queue and len(animal_details) < BATCH_SIZE:
                animal = self.queue.pop(0)
                details = self.fetch_animal_details(animal['id'])
                animal_details.append(details)
        return animal_details