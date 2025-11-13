# Arquitetura de Microsserviços

Esta implementação transforma a aplicação monolítica em uma arquitetura de microsserviços com API Gateway.

## Arquitetura

### 1. API Gateway (Porta 3000)
- **Responsabilidade**: Roteamento de requisições para os microsserviços
- **Tecnologia**: Node.js + Express + express-http-proxy
- **Rotas expostas**:
  - `/api/v1/auth/*` → API Auth
  - `/api/v1/projects/*` → API Dados
  - `/api/v1/tasks/*` → API Dados

### 2. API Dados (Porta 3001)
- **Responsabilidade**: Gerenciamento de projetos e tarefas
- **Tecnologia**: Node.js + Express
- **Rotas**:
  - `GET /projects` - Lista projetos
  - `POST /projects` - Cria projeto
  - `GET /projects/:id` - Busca projeto por ID
  - `PUT /projects/:id` - Atualiza projeto
  - `DELETE /projects/:id` - Remove projeto
  - `GET /tasks` - Lista tarefas
  - `GET /tasks/:id` - Busca tarefa por ID
  - `GET /projects/:projectId/tasks` - Lista tarefas do projeto
  - `POST /projects/:projectId/tasks` - Cria tarefa
  - `PUT /tasks/:id` - Atualiza tarefa
  - `DELETE /tasks/:id` - Remove tarefa

### 3. API Auth (Porta 3002)
- **Responsabilidade**: Autenticação e autorização
- **Tecnologia**: Node.js + Express + JWT + bcrypt
- **Rotas**:
  - `POST /auth/register` - Registro de usuário
  - `POST /auth/login` - Login
  - `POST /auth/validate` - Validação de token
  - `GET /auth/users` - Lista usuários (admin only)

## Como Executar

### Opção 1: Script Automático (Windows)
```bash
# Execute o script que inicia todos os serviços
install-and-start.bat
```

### Opção 2: Scripts Individuais
```bash
# Em 3 terminais separados, execute:
cd api-gateway && start.bat
cd api-dados && start.bat  
cd api-auth && start.bat
```

### Opção 3: Manual
```bash
# Terminal 1 - API Gateway
cd microservices/api-gateway
npm install
npm start

# Terminal 2 - API Dados
cd microservices/api-dados
npm install
npm start

# Terminal 3 - API Auth
cd microservices/api-auth
npm install
npm start
```

## Testando a API

### 1. Health Check
```bash
GET http://localhost:3000/health
GET http://localhost:3001/health
GET http://localhost:3002/health
```

### 2. Autenticação
```bash
# Registro
POST http://localhost:3000/api/v1/auth/register
{
  "email": "teste@example.com",
  "password": "123456",
  "name": "Usuário Teste"
}

# Login
POST http://localhost:3000/api/v1/auth/login
{
  "email": "admin@example.com",
  "password": "123456"
}
```

### 3. Projetos (via Gateway)
```bash
# Criar projeto
POST http://localhost:3000/api/v1/projects
{
  "title": "Projeto Teste",
  "description": "Descrição do projeto"
}

# Listar projetos
GET http://localhost:3000/api/v1/projects
```

### 4. Tarefas (via Gateway)
```bash
# Criar tarefa
POST http://localhost:3000/api/v1/projects/{project_id}/tasks
{
  "title": "Tarefa Teste",
  "description": "Descrição da tarefa",
  "assignedTo": "user-id"
}

# Listar tarefas do projeto
GET http://localhost:3000/api/v1/projects/{project_id}/tasks
```

## Usuários Pré-cadastrados

- **Admin**: admin@example.com / 123456
- **User**: user@example.com / 123456

## Isolamento dos Microsserviços

Os microsserviços rodam em portas diferentes e são acessíveis apenas através do Gateway na porta 3000. Em um ambiente de produção, as portas 3001 e 3002 estariam bloqueadas externamente.