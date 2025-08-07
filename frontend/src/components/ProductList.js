import React from 'react';

const ProductList = ({ products }) => {
  return (
    <div className="product-list-card">
      <h3 className="card-title">Product List</h3>
      <div className="product-table-container">
        <table className="product-table">
          <thead>
            <tr>
              <th>Product</th>
              <th>Category</th>
              <th>Quantity</th>
              <th>Price</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {products.length === 0 ? (
              <tr>
                <td colSpan="5" className="empty-list-message">No products in inventory.</td>
              </tr>
            ) : (
              products.map((product) => (
                <tr key={product.id}>
                  <td>{product.name}</td>
                  <td>{product.category || 'N/A'}</td>
                  <td>{product.quantity}</td>
                  <td>${product.price ? product.price.toFixed(2) : '0.00'}</td>
                  <td>
                    {/* Placeholder for Edit/Delete icons */}
                    <div className="actions-icons">
                      <span className="icon">✏️</span>
                      <span className="icon">🗑️</span>
                    </div>
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default ProductList;
