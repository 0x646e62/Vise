import axios from "axios";

const API_BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export const clientesService = {
  // Obtener todos los clientes
  getAll: async () => {
    const response = await api.get("/client");
    return response.data;
  },

  // Obtener un cliente por ID
  getById: async (id) => {
    const response = await api.get(`/client/${id}`);
    return response.data;
  },

  // Crear un nuevo cliente
  create: async (clientData) => {
    const response = await api.post("/client", clientData);
    return response.data;
  },

  // Actualizar un cliente
  update: async (id, clientData) => {
    const response = await api.put(`/client/${id}`, clientData);
    return response.data;
  },

  // Eliminar un cliente
  delete: async (id) => {
    const response = await api.delete(`/client/${id}`);
    return response.data;
  },
};

export default api;
