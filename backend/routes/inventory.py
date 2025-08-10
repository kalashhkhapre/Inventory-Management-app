from flask import Blueprint, jsonify, request
from services.inventory_service import get_all_products, create_new_product
from models import db, Product

inventory_bp = Blueprint('inventory_bp', __name__, url_prefix='/api')

@inventory_bp.route('/products', methods=['GET'])
def get_products():
    products = get_all_products()
    return jsonify([product.to_dict() for product in products])

@inventory_bp.route('/products', methods=['POST'])
def add_product():
    data = request.json
    new_product, error, status_code = create_new_product(data)
    if error:
        return jsonify({"error": error}), status_code
    return jsonify(new_product.to_dict()), status_code

@inventory_bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    try:
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500