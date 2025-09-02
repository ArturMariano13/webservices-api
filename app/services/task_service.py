from typing import List, Optional
from uuid import uuid4
from app.models.task import Task  # Importa a classe de modelo Task

# Simulação de um banco de dados em memória
# Agora com objetos da classe Task e IDs do tipo string (UUIDs)
in_memory_db = [
    Task(project_id=str(uuid4()), title='Task 1 - Project 1', assigned_to=str(uuid4()), description='This is the first task for Project 1'),
    Task(project_id=str(uuid4()), title='Task 2 - Project 1', assigned_to=str(uuid4()), description='This is the second task for Project 1'),
    Task(project_id=str(uuid4()), title='Task 3 - Project 2', assigned_to=str(uuid4()), description='This is the only task for Project 2')
]

# Note: Para manter a consistência, os project_id e assigned_to também são UUIDs.

class TaskService:
    def get_tasks_by_project_id(self, project_id: str) -> List[Task]:
        """Retorna todas as tarefas de um projeto específico."""
        return [task for task in in_memory_db if task.project_id == project_id]

    def get_all_tasks(self) -> List[Task]:
        """Retorna todas as tarefas (método auxiliar)."""
        return in_memory_db

    def get_task(self, task_id: str) -> Optional[Task]:
        """Retorna uma tarefa por ID."""
        for task in in_memory_db:
            if task.id == task_id:
                return task
        return None

    def create_task(self, new_task_data: dict) -> Task:
        """Cria uma nova tarefa a partir dos dados recebidos."""
        new_task = Task(
            project_id=new_task_data.get("projectId"),
            title=new_task_data.get("title"),
            description=new_task_data.get("description"),
            status=new_task_data.get("status"),
            due_date=new_task_data.get("dueDate"),
            assigned_to=new_task_data.get("assignedTo")
        )
        in_memory_db.append(new_task)
        return new_task

    def edit_task(self, task_id: str, task_changed_data: dict) -> Optional[Task]:
        """Atualiza uma tarefa existente por ID."""
        for task in in_memory_db:
            if task.id == task_id:
                if 'title' in task_changed_data:
                    task.title = task_changed_data['title']
                if 'description' in task_changed_data:
                    task.description = task_changed_data['description']
                if 'status' in task_changed_data:
                    task.status = task_changed_data['status']
                if 'due_date' in task_changed_data:
                    task.due_date = task_changed_data['due_date']
                if 'assigned_to' in task_changed_data:
                    task.assigned_to = task_changed_data['assigned_to']
                return task
        return None

    def delete_task(self, task_id: str) -> bool:
        """Deleta uma tarefa por ID."""
        for index, task in enumerate(in_memory_db):
            if task.id == task_id:
                del in_memory_db[index]
                return True
        return False