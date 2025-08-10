from models import db, Product

def get_all_products():
    """Fetches all products from the database."""
    return Product.query.all()

def create_new_product(data):
    """
    Creates a new product in the database.
    
    Args:
        data (dict): A dictionary containing 'name', 'category', 'quantity', and 'price'.
    
    Returns:
        tuple: A tuple containing (new_product_object, error_message, status_code).
    """
    if not data or 'name' not in data or 'quantity' not in data:
        return None, "Invalid data. 'name' and 'quantity' are required.", 400

    # Validate and convert types
    try:
        quantity = int(data['quantity'])
    except (ValueError, TypeError):
        return None, "'quantity' must be an integer.", 400

    price = None
    if 'price' in data and data['price'] is not None:
        try:
            price = float(data['price'])
        except (ValueError, TypeError):
            return None, "'price' must be a number.", 400

    if Product.query.filter_by(name=data['name']).first():
        return None, "Product with this name already exists.", 409

    new_product = Product(
        name=data['name'], 
        category=data.get('category'), # Use .get() for optional fields
        quantity=quantity,
        price=price # Use .get() for optional fields
    )
    try:
        db.session.add(new_product)
        db.session.commit()
        return new_product, None, 201
    except Exception as e:
        db.session.rollback()
        return None, str(e), 500
