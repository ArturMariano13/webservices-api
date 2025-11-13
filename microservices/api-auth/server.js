const express = require('express');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');
const cors = require('cors');
const { v4: uuidv4 } = require('uuid');

const app = express();
const PORT = 3002;
const JWT_SECRET = 'seu-jwt-secret-aqui';

app.use(cors());
app.use(express.json());

// Simulação de banco de dados de usuários
let users = [
  {
    id: uuidv4(),
    email: 'admin@example.com',
    password: bcrypt.hashSync('123456', 10),
    name: 'Administrador',
    role: 'admin'
  },
  {
    id: uuidv4(),
    email: 'user@example.com',
    password: bcrypt.hashSync('123456', 10),
    name: 'Usuário',
    role: 'user'
  }
];

// Middleware de logging
app.use((req, res, next) => {
  console.log(`${new Date().toISOString()} - API-AUTH - ${req.method} ${req.path}`);
  next();
});

// Health check
app.get('/health', (req, res) => {
  res.json({ service: 'api-auth', status: 'running', timestamp: new Date().toISOString() });
});

// Registro de usuário
app.post('/auth/register', async (req, res) => {
  const { email, password, name, role = 'user' } = req.body;

  if (!email || !password || !name) {
    return res.status(400).json({ error: 'Email, senha e nome são obrigatórios' });
  }

  // Verifica se usuário já existe
  const existingUser = users.find(u => u.email === email);
  if (existingUser) {
    return res.status(409).json({ error: 'Usuário já existe' });
  }

  const hashedPassword = await bcrypt.hash(password, 10);
  const user = {
    id: uuidv4(),
    email,
    password: hashedPassword,
    name,
    role,
    createdAt: new Date().toISOString()
  };

  users.push(user);

  const token = jwt.sign(
    { id: user.id, email: user.email, role: user.role },
    JWT_SECRET,
    { expiresIn: '24h' }
  );

  res.status(201).json({
    message: 'Usuário criado com sucesso',
    token,
    user: { id: user.id, email: user.email, name: user.name, role: user.role }
  });
});

// Login
app.post('/auth/login', async (req, res) => {
  const { email, password } = req.body;

  if (!email || !password) {
    return res.status(400).json({ error: 'Email e senha são obrigatórios' });
  }

  const user = users.find(u => u.email === email);
  if (!user) {
    return res.status(401).json({ error: 'Credenciais inválidas' });
  }

  const isValidPassword = await bcrypt.compare(password, user.password);
  if (!isValidPassword) {
    return res.status(401).json({ error: 'Credenciais inválidas' });
  }

  const token = jwt.sign(
    { id: user.id, email: user.email, role: user.role },
    JWT_SECRET,
    { expiresIn: '24h' }
  );

  res.json({
    message: 'Login realizado com sucesso',
    token,
    user: { id: user.id, email: user.email, name: user.name, role: user.role }
  });
});

// Validação de token
app.post('/auth/validate', (req, res) => {
  const token = req.headers.authorization?.replace('Bearer ', '');

  if (!token) {
    return res.status(401).json({ error: 'Token não fornecido' });
  }

  try {
    const decoded = jwt.verify(token, JWT_SECRET);
    const user = users.find(u => u.id === decoded.id);
    
    if (!user) {
      return res.status(401).json({ error: 'Usuário não encontrado' });
    }

    res.json({
      valid: true,
      user: { id: user.id, email: user.email, name: user.name, role: user.role }
    });
  } catch (error) {
    res.status(401).json({ error: 'Token inválido' });
  }
});

// Listar usuários (apenas para admin)
app.get('/auth/users', (req, res) => {
  const token = req.headers.authorization?.replace('Bearer ', '');

  if (!token) {
    return res.status(401).json({ error: 'Token não fornecido' });
  }

  try {
    const decoded = jwt.verify(token, JWT_SECRET);
    if (decoded.role !== 'admin') {
      return res.status(403).json({ error: 'Acesso negado' });
    }

    const usersList = users.map(u => ({
      id: u.id,
      email: u.email,
      name: u.name,
      role: u.role,
      createdAt: u.createdAt
    }));

    res.json(usersList);
  } catch (error) {
    res.status(401).json({ error: 'Token inválido' });
  }
});

app.listen(PORT, () => {
  console.log(`API-AUTH rodando na porta ${PORT}`);
});