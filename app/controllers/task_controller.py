from flask import Blueprint, jsonify, request, abort, Response
from app.services.task_service import TaskService
from flask import request


task_service = TaskService()
task_bp = Blueprint('tasks', __name__)

@task_bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks_list = task_service.get_all_tasks()
    return jsonify([task.to_dict() for task in tasks_list])

@task_bp.route('/tasks/<int:id>', methods=['GET'])
def get_task_by_id(id):
    task = task_service.get_task(id)
    if task:
        return jsonify(task)
    return jsonify({'message': 'Task not found'}), 404

@task_bp.route('/projects/<string:project_id>/tasks', methods=['GET'])
def get_tasks_by_project_id(project_id: str):
    """
    Retorna a lista de tarefas para um projeto específico.
    """
    tasks_list = task_service.get_tasks_by_project_id(project_id)
    
    # Se não houver tarefas, a lista retornada estará vazia.
    # O status 200 OK é o correto, mesmo que a lista esteja vazia.
    return jsonify([task.to_dict() for task in tasks_list])         


@task_bp.route('tasks/<string:task_id>', methods=['PUT'])
def edit_task_by_id(task_id: str):
    """
    Atualiza uma tarefa existente por ID.
    """
    data = request.get_json()

    # Validação básica de dados ausentes
    if not data:
        abort(400, description="Dados inválidos ou ausentes na requisição.")

    task = task_service.edit_task(task_id, data)

    if task:
        # Converte o objeto Task para um dicionário antes de retornar
        return jsonify(task.to_dict())
    
    # Retorna erro 404 se a tarefa não for encontrada
    abort(404, description="Tarefa não encontrada")

@task_bp.route('/tasks/<string:id>', methods=['DELETE'])
def delete_task_by_id(id):
    task = task_service.delete_task(id)
    if task:
        return jsonify({'message': 'Task deleted successfully!'})
    return jsonify({'message': 'Task not found'}), 404

@task_bp.route('/projects/<string:project_id>/tasks', methods=['POST'])
def create_task_for_project(project_id: str):
    """
    Cria uma nova tarefa para um projeto.
    """
    data = request.get_json()
    if not data:
        abort(400, description="Dados inválidos ou ausentes na requisição.")

    # Adiciona o project_id ao payload da tarefa
    data['projectId'] = project_id

    new_task = task_service.create_task(data)

    return jsonify(new_task.to_dict()), 201