import React, { useState, useEffect } from 'react';
import AddProductForm from './components/AddProductForm';
import ProductList from './components/ProductList';
import inventoryApi from './api/inventoryApi';

function App() {
  const [products, setProducts] = useState([]);

  const fetchProducts = async () => {
    const fetchedProducts = await inventoryApi.getProducts();
    setProducts(fetchedProducts);
  };

  useEffect(() => {
    fetchProducts();
  }, []);

  return (
    <div className="app-container">
      <header className="app-header">
        <h1>Kalash Inventory</h1>
        <div className="header-actions">
          {/* You can add a search bar or user icon here */}
        </div>
      </header>
      <main className="main-content">
        <AddProductForm onProductAdded={fetchProducts} />
        <ProductList products={products} />
      </main>
    </div>
  );
}

export default App;