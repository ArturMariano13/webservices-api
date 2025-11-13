const express = require('express');
const proxy = require('express-http-proxy');
const cors = require('cors');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

// Middleware de logging
app.use((req, res, next) => {
  console.log(`${new Date().toISOString()} - ${req.method} ${req.path}`);
  next();
});

// Rota de health check
app.get('/health', (req, res) => {
  res.json({ status: 'API Gateway is running', timestamp: new Date().toISOString() });
});

// Proxy para API de autenticação
app.use('/api/v1/auth', proxy(process.env.API_AUTH_URL, {
  proxyReqPathResolver: (req) => `/auth${req.url}`,
  proxyErrorHandler: (err, res, next) => {
    console.error('Erro no proxy auth:', err.message);
    res.status(503).json({ error: 'Serviço de autenticação indisponível' });
  }
}));

// Proxy para API de dados (projetos e tarefas)
app.use('/api/v1/projects', proxy(process.env.API_DADOS_URL, {
  proxyReqPathResolver: (req) => `/projects${req.url}`,
  proxyErrorHandler: (err, res, next) => {
    console.error('Erro no proxy dados:', err.message);
    res.status(503).json({ error: 'Serviço de dados indisponível' });
  }
}));

app.use('/api/v1/tasks', proxy(process.env.API_DADOS_URL, {
  proxyReqPathResolver: (req) => `/tasks${req.url}`,
  proxyErrorHandler: (err, res, next) => {
    console.error('Erro no proxy dados:', err.message);
    res.status(503).json({ error: 'Serviço de dados indisponível' });
  }
}));

// Rota 404 para rotas não encontradas
app.use('*', (req, res) => {
  res.status(404).json({ error: 'Rota não encontrada' });
});

app.listen(PORT, () => {
  console.log(`API Gateway rodando na porta ${PORT}`);
  console.log(`API Dados: ${process.env.API_DADOS_URL}`);
  console.log(`API Auth: ${process.env.API_AUTH_URL}`);
});