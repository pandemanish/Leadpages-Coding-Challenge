from datetime import datetime, timezone

class Transformer:
    def __init__(self):
        pass

    def apply_transformation(self, animal_details=None, multiple=False) -> dict:
        if multiple:
            for animal in animal_details:
                animal = self.transform_field_friends(animal)
                animal = self.transform_field_born_at(animal)
        else:
            animal = self.transform_field_friends(animal)
            animal = self.transform_field_born_at(animal)
        return animal_details

    def transform_field_friends(self, animal):
        if 'friends' in animal and isinstance(animal['friends'], str):
            animal['friends'] = animal['friends'].split(',')
        return animal

    def transform_field_born_at(self, animal):
        if 'born_at' in animal and animal['born_at']:
            iso_time_format = datetime.fromtimestamp(animal['born_at'] / 1000, tz=timezone.utc).isoformat()
            animal['born_at'] = iso_time_format
