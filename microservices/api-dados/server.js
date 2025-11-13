const express = require('express');
const cors = require('cors');
const { v4: uuidv4 } = require('uuid');

const app = express();
const PORT = 3001;

app.use(cors());
app.use(express.json());

// Simulação de banco de dados em memória
let projects = [];
let tasks = [];

// Middleware de logging
app.use((req, res, next) => {
  console.log(`${new Date().toISOString()} - API-DADOS - ${req.method} ${req.path}`);
  next();
});

// Health check
app.get('/health', (req, res) => {
  res.json({ service: 'api-dados', status: 'running', timestamp: new Date().toISOString() });
});

// ROTAS DE PROJETOS
app.get('/projects', (req, res) => {
  res.json(projects);
});

app.get('/projects/:id', (req, res) => {
  const project = projects.find(p => p.id === req.params.id);
  if (!project) {
    return res.status(404).json({ error: 'Projeto não encontrado' });
  }
  res.json(project);
});

app.post('/projects', (req, res) => {
  const { title, description, status = 'ativo' } = req.body;
  
  if (!title || !description) {
    return res.status(400).json({ error: 'Título e descrição são obrigatórios' });
  }

  const project = {
    id: uuidv4(),
    title,
    description,
    status,
    createdAt: new Date().toISOString()
  };

  projects.push(project);
  res.status(201).json(project);
});

app.put('/projects/:id', (req, res) => {
  const projectIndex = projects.findIndex(p => p.id === req.params.id);
  if (projectIndex === -1) {
    return res.status(404).json({ error: 'Projeto não encontrado' });
  }

  const { title, description, status } = req.body;
  projects[projectIndex] = { ...projects[projectIndex], title, description, status };
  res.json(projects[projectIndex]);
});

app.delete('/projects/:id', (req, res) => {
  const projectIndex = projects.findIndex(p => p.id === req.params.id);
  if (projectIndex === -1) {
    return res.status(404).json({ error: 'Projeto não encontrado' });
  }

  projects.splice(projectIndex, 1);
  tasks = tasks.filter(t => t.projectId !== req.params.id);
  res.status(204).send();
});

// ROTAS DE TAREFAS
app.get('/tasks', (req, res) => {
  res.json(tasks);
});

app.get('/tasks/:id', (req, res) => {
  const task = tasks.find(t => t.id === req.params.id);
  if (!task) {
    return res.status(404).json({ error: 'Tarefa não encontrada' });
  }
  res.json(task);
});

app.get('/projects/:projectId/tasks', (req, res) => {
  const projectTasks = tasks.filter(t => t.projectId === req.params.projectId);
  res.json(projectTasks);
});

app.post('/projects/:projectId/tasks', (req, res) => {
  const { title, description, status = 'a_fazer', dueDate, assignedTo } = req.body;
  
  if (!title || !description || !assignedTo) {
    return res.status(400).json({ error: 'Título, descrição e responsável são obrigatórios' });
  }

  const task = {
    id: uuidv4(),
    projectId: req.params.projectId,
    title,
    description,
    status,
    dueDate,
    assignedTo,
    createdAt: new Date().toISOString()
  };

  tasks.push(task);
  res.status(201).json(task);
});

app.put('/tasks/:id', (req, res) => {
  const taskIndex = tasks.findIndex(t => t.id === req.params.id);
  if (taskIndex === -1) {
    return res.status(404).json({ error: 'Tarefa não encontrada' });
  }

  const { title, description, status, dueDate, assignedTo } = req.body;
  tasks[taskIndex] = { ...tasks[taskIndex], title, description, status, dueDate, assignedTo };
  res.json(tasks[taskIndex]);
});

app.delete('/tasks/:id', (req, res) => {
  const taskIndex = tasks.findIndex(t => t.id === req.params.id);
  if (taskIndex === -1) {
    return res.status(404).json({ error: 'Tarefa não encontrada' });
  }

  tasks.splice(taskIndex, 1);
  res.status(204).send();
});

app.listen(PORT, () => {
  console.log(`API-DADOS rodando na porta ${PORT}`);
});