import React from 'react';

const ProductList = ({ products }) => {
  return (
    <div className="product-list-card">
      <h3>Product List</h3>
      <div className="product-table">
        <div className="table-header">
          <div>Product</div>
          <div>Quantity</div>
        </div>
        {products.length === 0 ? (
          <div className="empty-list-message">No products in inventory.</div>
        ) : (
          products.map((product) => (
            <div key={product.id} className="table-row">
              <div>{product.name}</div>
              <div>{product.quantity}</div>
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default ProductList;