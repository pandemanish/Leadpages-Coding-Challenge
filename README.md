# Leadpages-Coding-Challenge
Leadpages Coding Challenge for Animal Data Processing
This python project fetches data from the given API, processes it and Posts the processed data to the given API. It's designed to be resilient to errors and handles them gracefully.

Prerequisites
Python 3.6 or higher

Instructions to run the project
1. Clone this project
2. Run the command "pip install -r requirements.txt" to install all the dependencies
3. Create a .env file at the root if the project and add BASE_URL and BATCH_SIZE as environment variables
4. Run the command "python run.py" to start the project
5. Logs stored in logs/info.log file


The pipeline consists of five main components:
1. Extractor: This component fetches data from the given API and returns it as a list of dictionaries in batches.
2. Transformer: This component processes the data fetched by the Extractor. Two transformations are applied to the data:
    a. The friend field is split into a list of friend names.
    b. The born_at field is translated into an ISO8601 timestamp in UTC..
3. Loader: This component posts the processed data to the given API.
4. Main: This component orchestrates the pipeline.
5. Client: This component is responsible for making HTTP requests to the given API. It's designed to be resilient to errors and handles them gracefully.

The run.py script runs the pipeline. It initializes the Extractor, Transformer, Loader, and Client components, and then orchestrates the pipeline by calling the Extractor, Transformer, and Loader components in sequence.

Logging
The project uses the logging module to log information about the execution of the pipeline. The logs are stored in the logs/info.log file.

Running Tests
To run tests:
1. Run the command "pytest" to run the tests
2. Logs stored in logs/info.log file
