import os
from flask import Flask
from config import DevelopmentConfig, ProductionConfig
from models import configure_db
from routes.inventory import inventory_bp
from routes.auth import auth_bp
from flask_cors import CORS
from time import sleep

def create_app():
    app = Flask(__name__)
    
    # Configure app based on environment
    app_settings = os.environ.get('APP_SETTINGS', 'config.DevelopmentConfig')
    app.config.from_object(app_settings)

    # Enable CORS for the frontend
    CORS(app)

    # Configure and initialize the database
    configure_db(app)

    # Wait for the MySQL container to be ready
    sleep(15) 

    # Register blueprints
    app.register_blueprint(inventory_bp)
    app.register_blueprint(auth_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)