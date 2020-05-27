from section6.app import app
from section6.db import db

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all() # Create Tables Automatically into DB as per model classes