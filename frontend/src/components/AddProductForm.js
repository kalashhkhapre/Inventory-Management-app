import React, { useState } from 'react';
import inventoryApi from '../api/inventoryApi';

const AddProductForm = ({ onProductAdded }) => {
  const [name, setName] = useState('');
  const [quantity, setQuantity] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const newProduct = { name, quantity: parseInt(quantity) };
      await inventoryApi.addProduct(newProduct);
      onProductAdded();
      setName('');
      setQuantity('');
    } catch (error) {
      alert('Failed to add product!');
    }
  };

  return (
    <div className="add-product-card">
      <h3>Add New Product</h3>
      <form onSubmit={handleSubmit} className="product-form">
        <input
          type="text"
          placeholder="Product Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
          className="form-input"
        />
        <input
          type="number"
          placeholder="Quantity"
          value={quantity}
          onChange={(e) => setQuantity(e.target.value)}
          required
          className="form-input"
        />
        <button type="submit" className="add-button">Add Product</button>
      </form>
    </div>
  );
};

export default AddProductForm;