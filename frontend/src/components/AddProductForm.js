import React, { useState } from 'react';
import inventoryApi from '../api/inventoryApi';

const AddProductForm = ({ onProductAdded }) => {
  const [name, setName] = useState('');
  const [category, setCategory] = useState('');
  const [quantity, setQuantity] = useState('');
  const [price, setPrice] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const newProduct = { 
        name, 
        category,
        quantity: parseInt(quantity), 
        price: parseFloat(price) 
      };
      await inventoryApi.addProduct(newProduct);
      onProductAdded();
      setName('');
      setCategory('');
      setQuantity('');
      setPrice('');
    } catch (error) {
      alert('Failed to add product!');
    }
  };

  return (
    <div className="add-product-card">
      <h3 className="card-title">Add New Product</h3>
      <form onSubmit={handleSubmit} className="product-form">
        <label className="form-label">Product Name</label>
        <input
          type="text"
          placeholder="Product Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
          className="form-input"
        />
        
        <label className="form-label">Category</label>
        <input
          type="text"
          placeholder="Category"
          value={category}
          onChange={(e) => setCategory(e.target.value)}
          className="form-input"
        />

        <label className="form-label">Quantity</label>
        <input
          type="number"
          placeholder="Quantity"
          value={quantity}
          onChange={(e) => setQuantity(e.target.value)}
          required
          className="form-input"
        />

        <label className="form-label">Price</label>
        <input
          type="number"
          placeholder="Price"
          value={price}
          onChange={(e) => setPrice(e.target.value)}
          required
          className="form-input"
        />

        <button type="submit" className="add-button">Add Product</button>
      </form>
    </div>
  );
};

export default AddProductForm;
