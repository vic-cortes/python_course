import json
from datetime import datetime

import pandas as pd
from flask import Flask, jsonify, redirect, render_template, request, session, url_for

# Create Flask app
app = Flask(__name__)
app.secret_key = "your-secret-key-here"  # Needed for sessions

# In-memory data storage (use database in production)
users = []
posts = []


# Home page
@app.route("/")
def home():
    return "Hello from virtual environment!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
