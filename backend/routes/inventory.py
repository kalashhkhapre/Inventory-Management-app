from flask import Blueprint, jsonify, request
from services.inventory_service import get_all_products, create_new_product

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