from typing import List, Optional
from uuid import uuid4
from app.models.project import Project  # Apenas a classe Project

# Simulação de um banco de dados em memória
# Agora com objetos da classe Project e IDs do tipo string (UUIDs)
in_memory_db = [
    Project(title='Project 1', description='Project Description 1'),
    Project(title='Project 2', description='Project Description 2'),
    Project(title='Project 3', description='Project Description 3')
]

# Acessa os objetos e atualiza os IDs para serem únicos
in_memory_db[0].id = str(uuid4())
in_memory_db[1].id = str(uuid4())
in_memory_db[2].id = str(uuid4())

class ProjectService:
    def get_all_projects(self) -> List[Project]:
        """Retorna todos os projetos."""
        return in_memory_db

    def get_project(self, project_id: str) -> Optional[Project]:
        """Retorna um projeto por ID."""
        for project in in_memory_db:
            if project.id == project_id:
                return project
        return None

    def create_project(self, project_data: dict) -> Project:
        """Cria um novo projeto a partir dos dados recebidos."""
        new_project = Project(
            title=project_data.get("title"),
            description=project_data.get("description"),
            status=project_data.get("status", "ativo")
        )
        in_memory_db.append(new_project)
        return new_project

    def edit_project(self, project_id: str, project_changed: dict) -> Optional[Project]:
        """Atualiza um projeto existente por ID."""
        for project in in_memory_db:
            if project.id == project_id:
                if 'title' in project_changed:
                    project.title = project_changed['title']
                if 'description' in project_changed:
                    project.description = project_changed['description']
                if 'status' in project_changed:
                    project.status = project_changed['status']
                return project
        return None

    def delete_project(self, project_id: str) -> bool:
        """Deleta um projeto por ID."""
        for index, project in enumerate(in_memory_db):
            if project.id == project_id:
                del in_memory_db[index]
                return True
        return False