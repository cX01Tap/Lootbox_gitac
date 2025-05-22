from flask import Flask

app = Flask(__name__)

# Configuration settings can be added here

from .app import *  # Import routes from app.py