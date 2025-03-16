"""Credentials for hw flask server."""
from os import getenv

from dotenv import load_dotenv
from flask import Flask

from extras import DEFAULT_PORT

load_dotenv()

app = Flask(__name__)
app.json.ensure_ascii = False


FLASK_PORT = int(getenv('FLASK_PORT', default=DEFAULT_PORT))
