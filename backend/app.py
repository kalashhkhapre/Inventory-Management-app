import os
import time
import logging
from flask import Flask
from flask_cors import CORS
from sqlalchemy.exc import OperationalError, InterfaceError
from models import db
from routes.inventory import inventory_bp
from routes.auth import auth_bp
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)

    # Load configuration
    from config import DevelopmentConfig, ProductionConfig
    app_settings = os.environ.get('APP_SETTINGS', 'config.DevelopmentConfig')

    if app_settings == "config.ProductionConfig":
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    # Configure logging
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")

    # Add debug logging for database configuration
    logging.info(f"Database URI: {app.config.get('SQLALCHEMY_DATABASE_URI', 'Not set')}")
    logging.info(f"Environment: {app_settings}")

    CORS(app)
    db.init_app(app)
    Migrate(app, db)  # Flask-Migrate for DB migrations

    # Only wait for DB if not in migration mode
    if not _is_migration_command():
        _wait_for_db(app)

    # Register blueprints
    app.register_blueprint(inventory_bp)
    app.register_blueprint(auth_bp)

    @app.route("/health")
    def health():
        return {"status": "OK"}, 200

    @app.route("/")
    def index():
        return {"message": "Inventory Management API", "status": "running"}, 200

    return app


def _is_migration_command():
    """Check if we're running a Flask migration command"""
    import sys
    return any(cmd in sys.argv for cmd in ['db', 'migrate', 'upgrade', 'downgrade'])


def _wait_for_db(app, retries=10, delay=5):
    """Retry DB connection before starting app."""
    logging.info("Attempting to connect to database...")
    
    for attempt in range(1, retries + 1):
        try:
            with app.app_context():
                # Test basic connection
                result = db.session.execute("SELECT 1").fetchone()
                logging.info(f"Database connection established successfully. Test query result: {result}")
                
                # Create tables if they don't exist
                db.create_all()
                logging.info("Database tables created/verified.")
                return
                
        except (OperationalError, InterfaceError) as e:
            error_msg = str(e)
            logging.warning(f"[DB INIT] Attempt {attempt}/{retries} failed: {error_msg}")
            
            # Provide specific error guidance
            if "Name or service not known" in error_msg:
                logging.error("❌ MySQL server hostname cannot be resolved. Check if MySQL is running and hostname is correct.")
            elif "Connection refused" in error_msg:
                logging.error("❌ MySQL server is not accepting connections. Check if MySQL service is running.")
            elif "Access denied" in error_msg:
                logging.error("❌ MySQL authentication failed. Check username/password in .env file.")
            elif "Unknown database" in error_msg:
                logging.error("❌ Database does not exist. Create the database first.")
            else:
                logging.error(f"❌ Database connection error: {error_msg}")
            
            if attempt < retries:
                logging.info(f"⏳ Retrying in {delay} seconds...")
                time.sleep(delay)
            
        except Exception as e:
            logging.error(f"[DB INIT] Unexpected error on attempt {attempt}/{retries}: {e}")
            if attempt < retries:
                time.sleep(delay)
    
    # If we get here, all retries failed
    logging.error("❌ Database connection failed after multiple retries.")
    logging.error("🔧 Troubleshooting steps:")
    logging.error("   1. Check if MySQL server is running: sudo systemctl status mysql")
    logging.error("   2. Verify .env file exists with correct database credentials")
    logging.error("   3. Create database: mysql -u root -p -e 'CREATE DATABASE demodb;'")
    logging.error("   4. Test connection: mysql -u root -p -h localhost demodb")
    exit(1)


def print_startup_info():
    """Print helpful startup information"""
    print("\n" + "="*50)
    print("🚀 INVENTORY MANAGEMENT API")
    print("="*50)
    print(f"📊 Environment: {os.environ.get('FLASK_ENV', 'development')}")
    print(f"🔗 Database: {os.environ.get('MYSQL_DATABASE', 'demodb')}")
    print(f"🌐 Host: {os.environ.get('MYSQL_HOST', 'localhost')}")
    print(f"🔌 Port: {os.environ.get('MYSQL_PORT', '3306')}")
    print("="*50)
    print("📋 Available endpoints:")
    print("   GET  /health - Health check")
    print("   GET  / - API info")
    print("   API routes available via blueprints")
    print("="*50 + "\n")


if __name__ == '__main__':
    print_startup_info()
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)