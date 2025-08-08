import os
import time
from flask import Flask
from flask_cors import CORS
from sqlalchemy.exc import OperationalError
from models import db
from routes.inventory import inventory_bp
from routes.auth import auth_bp

def create_app():
    """Factory function to create and configure the Flask app."""
    app = Flask(__name__)
    
    # Use environment variable to select configuration
    app_settings = os.environ.get('APP_SETTINGS', 'config.DevelopmentConfig')
    app.config.from_object(app_settings)

    # Enable Cross-Origin Resource Sharing (CORS) for the frontend
    CORS(app)

    # Initialize the SQLAlchemy instance with the app here
    db.init_app(app)

    # Add a robust retry loop to wait for the database connection
    max_retries = 10
    retry_delay = 5  # seconds
    for i in range(max_retries):
        try:
            with app.app_context():
                db.create_all()
            print("Successfully connected to the database!")
            break  # Exit the loop on success
        except OperationalError:
            print(f"Attempt {i+1} of {max_retries}: Could not connect to the database. Retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)
    else:
        # This code runs if the loop completes without a 'break'
        print("Could not connect to the database after multiple retries. Exiting.")
        exit(1)

    # Register blueprints (routes)
    app.register_blueprint(inventory_bp)
    app.register_blueprint(auth_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
