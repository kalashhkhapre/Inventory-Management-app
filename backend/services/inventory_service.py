from models import db, Product

def get_all_products():
    """Fetches all products from the database."""
    return Product.query.all()

def create_new_product(data):
    """Creates a new product in the database."""
    if not data or 'name' not in data or 'quantity' not in data:
        return None, "Invalid data", 400
    
    new_product = Product(name=data['name'], quantity=data['quantity'])
    db.session.add(new_product)
    db.session.commit()
    return new_product, None, 201