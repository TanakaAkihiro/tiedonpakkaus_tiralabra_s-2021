import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

FILENAME = os.getenv('FILENAME') or 'text.txt'
FILE_PATH = os.path.join(dirname, '..', 'files', FILENAME)
