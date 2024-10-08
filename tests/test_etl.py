from pipeline.transformer import Transformer
from pipeline.extractor import Extractor
from pipeline.loader import Loader

# Mock API Client
class MockAPIClient:
    def fetch_animals_list(self, page):
        return {'total_pages':1, 'items': [{'id': 0, 'name': 'Boar', 'born_at': None, 'friends': 'Heron,Weasel'}, {'id': 1, 'name': 'Emu', 'born_at': None, 'friends': 'Goat,Weasel,Wolverine,Ferret'}]}
    
    def fetch_animal_details(self, id):
        return {'id': id, 'name': 'Boar', 'born_at': None, 'friends': 'Heron,Weasel'}
    
    def post_batch(self, animals):
        return {'message': 'Helped 2 find home'}


class TestETL:

    def test_extractor(self):
        extractor = Extractor(MockAPIClient())
        batch = extractor.get_next_animals_batch()

        assert len(batch) == 2
        print(batch[0], batch[1])
        assert batch[0]["id"] == 0
        assert batch[1]["id"] == 1

    # Transform a single animal's details with valid 'friends' and 'born_at' fields
    def test_transform_single_animal_details(self):
        transformer = Transformer()
        animal_details = {
            'name': 'Lion',
            'friends': 'Tiger,Elephant',
            'born_at': 1633072800000  # Equivalent to 2021-10-01T07:20:00Z
        }
        expected_result = {
            'name': 'Lion',
            'friends': ['Tiger', 'Elephant'],
            'born_at': '2021-10-01T07:20:00Z'
        }
        result = transformer.apply_transformation(animal_details)
        assert result == expected_result

    # Handle empty 'animal_details' input gracefully
    def test_handle_empty_animal_details(self):
        transformer = Transformer()
        animal_details = {}
        expected_result = {}
        result = transformer.apply_transformation(animal_details)
        assert result == expected_result

    # Transforms 'friends' field from a comma-separated string to a list
    def test_transforms_friends_field_to_list(self):
        transformer = Transformer()
        animal = {'name': 'Lion', 'friends': 'Tiger,Elephant'}
        result = transformer.transform_field_friends(animal)
        assert result['friends'] == ['Tiger', 'Elephant']

    # Handles 'friends' field not present in the animal dictionary
    def test_handles_missing_friends_field(self):
        transformer = Transformer()
        animal = {'name': 'Lion'}
        result = transformer.transform_field_friends(animal)
        assert 'friends' not in result
    


    # Converts Unix timestamp in milliseconds to ISO 8601 format
    def test_convert_unix_timestamp_to_iso_format(self):
        transformer = Transformer()
        animal = {'born_at': 1633072800000}  # Corresponds to 2021-10-01T00:00:00Z
        transformer.transform_field_born_at(animal)
        assert animal['born_at'] == '2021-10-01T07:20:00Z'

    # Handles 'born_at' field missing in the animal dictionary
    def test_handle_missing_born_at_field(self):
        transformer = Transformer()
        animal = {}  # 'born_at' field is missing
        transformer.transform_field_born_at(animal)
        assert 'born_at' not in animal

    
    def test_load(self):
        mock_api_client = MockAPIClient()
        loader = Loader(mock_api_client)
        
        animals = [
            {"id": 1, "name": "Lion", "born_at": "2021-03-30T12:30:38.888Z", "friends": ["Tiger", "Giraffe", "Zebra"]},
            {"id": 2, "name": "Elephant", "born_at": "2021-04-01T10:15:00.000Z", "friends": ["Rhino", "Hippo"]}
        ]
        
        response = loader.load_animals(animals)
        
        assert "message" in response