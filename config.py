import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL=os.getenv("BASE_URL") or "http://localhost:3123/animals/v1"
BATCH_SIZE:int=int(os.getenv("BATCH_SIZE")) or 100
STOP_AFTER_ATTEMPT:int=int(os.getenv("STOP_AFTER_ATTEMPT")) or 10
WAIT_FIXED:int=int(os.getenv("WAIT_FIXED")) or 2