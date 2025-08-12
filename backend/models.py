from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BaseModel(db.Model):
    """Base model with common fields."""
    __abstract__ = True

    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now(), nullable=False)

    def to_dict(self):
        """Converts model instance to dictionary."""
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class Product(BaseModel):
    """Represents the 'products' table."""
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    category = db.Column(db.String(80), nullable=True)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    price = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f"<Product {self.id} - {self.name}>"
