from flask_sqlalchemy import SQLAlchemy

# Create an instance of SQLAlchemy, but don't initialize it here.
# It will be initialized in app.py.
db = SQLAlchemy()

class Product(db.Model):
    """Represents the 'products' table in the database."""
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    category = db.Column(db.String(80), nullable=True)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    price = db.Column(db.Float, nullable=True)

    def to_dict(self):
        """Converts the product object to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'quantity': self.quantity,
            'price': self.price
        }
