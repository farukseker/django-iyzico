
import axios from "axios";

// API URL'sini uygun şekilde güncelle
const API_BASE_URL = "http://localhost:8000/api/"; 

// Token'ı storage'dan alma fonksiyonu
const getToken = () => localStorage.getItem("token") || sessionStorage.getItem("token");

// Axios instance oluştur
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

// Request interceptor: Her isteğe JWT token ekler
api.interceptors.request.use(
  (config) => {
    const token = getToken();
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Response interceptor: 401 hatası alınırsa kullanıcıyı çıkışa zorlar
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response && error.response.status === 401) {
      console.warn("Yetkisiz erişim, çıkış yapılıyor...");
      localStorage.removeItem("token");
      sessionStorage.removeItem("token");
      // window.location.href = "/login"; // Kullanıcıyı login sayfasına yönlendir
    }
    return Promise.reject(error);
  }
);

export default api;
