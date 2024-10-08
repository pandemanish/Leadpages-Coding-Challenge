from pipeline.logger import Logger
from pipeline.extractor import Extractor
from pipeline.client import Client
from pipeline.loader import Loader
from pipeline.transformer import Transformer


def main():
    # Initialize the pipeline components
    
    logger = Logger()
    client = Client(headers={})
    
    extractor = Extractor(client)
    transformer = Transformer()
    loader =  Loader(client)
    
    
    logger.info("Starting the pipeline...")
    page = 1
    while True:
        # Fetching the batch of animals
        logger.info(f"Fetching {page} batch of animals...")
        animals_batch = extractor.get_next_animals_batch()
        logger.notify(f"FETCHED animals details list: {animals_batch}")
        if not animals_batch:
            logger.info("Processing complete. Exiting.")
            break
        
       
       # Process the batch of animals
        logger.info(f"Processing batch of {len(animals_batch)} from batch {page} animals...")
        animals_batch = transformer.apply_transformation(animals_batch, multiple=True)
        logger.info(f"Finished processing batch of {len(animals_batch)} animals.")


        # Loading the batch of animals
        logger.info(f"Loading batch of {len(animals_batch)} from batch {page} animals...")
        response = loader.load_animals(animals_batch)
        logger.info(f"Finished loading batch of {len(animals_batch)} animals. Response:{response}")
        page += 1
    
    logger.info("Pipeline execution completed.")

if __name__ == "__main__":
    main()