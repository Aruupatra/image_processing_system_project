from app import app, db
from services.database import ProcessingRequest  # Import your models

with app.app_context():
    db.create_all()  # This creates all tables defined by the models
    print("Database tables created successfully.")
