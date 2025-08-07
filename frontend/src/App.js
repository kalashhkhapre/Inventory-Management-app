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
        <div className="logo">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 2L2 7V17L12 22L22 17V7L12 2Z" stroke="#6a67f0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M2 7L12 12L22 7" stroke="#6a67f0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M12 22V12" stroke="#6a67f0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <h1>Inventory management system made by kalash</h1>
        </div>
        <div className="header-actions">
          <input type="text" placeholder="Search" className="search-input" />
          <div className="user-icon">👤</div>
        </div>
      </header>
      <main className="main-content">
        <div className="left-panel">
          <AddProductForm onProductAdded={fetchProducts} />
        </div>
        <div className="right-panel">
          <ProductList products={products} />
        </div>
      </main>
    </div>
  );
}

export default App;
