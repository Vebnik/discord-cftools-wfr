from dotenv import load_dotenv; load_dotenv()
import os, logging

# logger
logging.basicConfig(level=logging.INFO)


# tests
def test_get_get_auth_token():
  assert isinstance('auth_data.token', str) == True
