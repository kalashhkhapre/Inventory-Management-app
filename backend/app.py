import os
from flask import Flask
from flask_cors import CORS
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

    # With the app context, create all the database tables
    with app.app_context():
        # This will create the database tables based on the models if they don't exist.
        db.create_all() 

    # Register blueprints (routes)
    app.register_blueprint(inventory_bp)
    app.register_blueprint(auth_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
