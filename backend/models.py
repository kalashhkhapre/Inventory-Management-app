from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def configure_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'quantity': self.quantity
        }