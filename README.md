# API de Gerenciamento de Tarefas e Projetos

Esta é uma API RESTful para gerenciar projetos e tarefas, desenvolvida como parte da disciplina de Serviços Web. A API segue o padrão de arquitetura **Controller, Service, Model** e é implementada com Flask.

## 1. Estrutura do Projeto

O projeto é organizado em camadas para garantir a separação de responsabilidades e facilitar a manutenção.

`app/main.py`: Ponto de entrada da aplicação.

`app/controllers/`: Responsável por rotear as requisições HTTP e chamar os serviços.

`app/services/`: Contém a lógica de negócio e a simulação do banco de dados.

`app/models/`: Define a estrutura de dados (classes Project e Task).


## 2. Como Executar

Siga os passos abaixo para rodar a API localmente.

### Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes do Python)

### Passos
- Crie o Ambiente Virtual:

`python -m venv venv`

- Ative o Ambiente Virtual:
    - Windows: `venv\Scripts\activate`
    - macOS/Linux: `source venv/bin/activate`

- Instale as Dependências:
    
`pip install -r requirements.txt`

- Execute a Aplicação:

`python -m app.main`


## 3. Endpoints da API

Todos os endpoints da API estão acessíveis sob o prefixo `/api/v1/`.

### Recurso: Projetos (`/projects`)

| **Método** | **Caminho**                   | **Descrição**                  |
|------------|-------------------------------|--------------------------------|
| **GET**    | /api/v1/projects              | Lista todos os projetos.       |
| **POST**   | /api/v1/projects              | Cria um novo projeto.          |
| **GET**    | /api/v1/projects/{project_id} | Retorna um projeto por ID.     |
| **PUT**    | /api/v1/projects/{project_id} | Atualiza um projeto existente. |
| **DELETE** | /api/v1/projects/{project_id} | Deleta um projeto.             |

### Recurso: Tarefas (`/tasks`)

| **Método** | **Caminho**                         | **Descrição**                         |
|------------|-------------------------------------|---------------------------------------|
| **GET**    | /api/v1/projects/{project_id}/tasks | Lista todas as tarefas de um projeto. |
| **POST**   | /api/v1/projects/{project_id}/tasks | Cria uma nova tarefa para um projeto. |
| **GET****  | /api/v1/tasks/{task_id}             | Retorna uma tarefa por ID.            |
| **PUT**    | /api/v1/tasks/{task_id}             | Atualiza uma tarefa existente.        |
| **DELETE** | /api/v1/tasks/{task_id}             | Deleta uma tarefa.                    |

## 4. Documentação OpenAPI

A especificação completa da API está disponível no arquivo openapi.yaml na raiz do projeto. Você pode visualizá-la em qualquer editor compatível com OpenAPI 3.0, como o Swagger Editor.