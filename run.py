import os
import requests
from dotenv import load_dotenv
from pipeline.logger import Logger
from datetime import datetime, timezone


load_dotenv()

logger = Logger()

CONFIG = {
    "base_url": os.getenv("BASE_URL") or "http://localhost:3123/animals/v1/",
    "batch_size": 100
}

def fetch_animals_list(page=1):
    return requests.get(f"{CONFIG['base_url']}/animals?page={page}").json()

def fetch_animal_details(self, animal_id):
    return requests.get(f"{CONFIG['base_url']}/animals/{animal_id}").json()

def transform_field_friends(animal):
    if 'friends' in animal and isinstance(animal['friends'], str):
        animal['friends'] = animal['friends'].split(',')

def transform_field_born_at(animal):
    if 'born_at' in animal and animal['born_at']:
        iso_time_format = datetime.fromtimestamp(animal['born_at'] / 1000, tz=timezone.utc).isoformat()
        animal['born_at'] = iso_time_format

def main():
    base_url = CONFIG["base_url"]
    batch_size = CONFIG["batch_size"]

