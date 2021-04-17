import axios from 'axios';

// Criar a URL base para consultar NODE que estará rodando o server na porta 3333
const api = axios.create({
    baseURL: 'http://localhost:3333'
});

export default api;
