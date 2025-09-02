from flask import Blueprint, jsonify, request, abort, Response
from app.services.project_service import ProjectService

project_service = ProjectService()
project_bp = Blueprint('projects', __name__)

@project_bp.route('/', methods=['GET'])
def get_projects():
    """
    Lista todos os projetos.
    """
    projects_list = project_service.get_all_projects()
    # Converte cada objeto Project para um dicionário antes de retornar como JSON
    return jsonify([project.to_dict() for project in projects_list])

@project_bp.route('/<string:project_id>', methods=['GET'])
def get_project_by_id(project_id):
    """
    Retorna um projeto por ID.
    """
    project = project_service.get_project(project_id)
    if project:
        # Converte o objeto Project para um dicionário
        return jsonify(project.to_dict())
    
    # Se o projeto não for encontrado, retorna um erro 404
    abort(404, description="Projeto não encontrado")

@project_bp.route('/', methods=['POST'])
def create_project():
    """
    Cria um novo projeto.
    """
    data = request.get_json()
    if not data:
        abort(400, description="Dados inválidos ou ausentes na requisição.")
    
    new_project = project_service.create_project(data)
    
    # Retorna o projeto criado com o código de status 201 Created
    return jsonify(new_project.to_dict()), 201

@project_bp.route('/<string:project_id>', methods=['PUT'])
def edit_project_by_id(project_id):
    """
    Atualiza um projeto existente por ID.
    """
    data = request.get_json()
    if not data:
        abort(400, description="Dados inválidos ou ausentes na requisição.")
        
    project = project_service.edit_project(project_id, data)
    if project:
        return jsonify(project.to_dict())
    
    abort(404, description="Projeto não encontrado")

@project_bp.route('/<string:project_id>', methods=['DELETE'])
def delete_project_by_id(project_id):
    """
    Deleta um projeto por ID.
    """
    if project_service.delete_project(project_id):
        # Retorna o código de status 204 No Content
        return Response(status=204)
        
    abort(404, description="Projeto não encontrado")