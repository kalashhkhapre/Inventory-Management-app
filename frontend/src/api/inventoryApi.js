import axios from 'axios';

const API_URL = 'http://localhost:5000/api';

const inventoryApi = {
  getProducts: async () => {
    try {
      const response = await axios.get(`${API_URL}/products`);
      return response.data;
    } catch (error) {
      console.error('Error fetching products:', error);
      return [];
    }
  },

  addProduct: async (productData) => {
    try {
      const response = await axios.post(`${API_URL}/products`, productData);
      return response.data;
    } catch (error) {
      console.error('Error adding product:', error);
      throw error;
    }
  },
};

export default inventoryApi;