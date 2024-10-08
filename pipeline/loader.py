class Loader:
    def __init__(self, client):
        self.client = client

    def load_animals(self, animals):
        return self.client.post_batch(animals)
