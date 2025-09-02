from flask import Flask, jsonify, request

app = Flask(__name__)

# database simulation
projects = [
    {
        'id': 1,
        'title': 'Project 1',
        'description': 'Project Description 1'
    },
    {
        'id': 2,
        'title': 'Project 2',
        'description': 'Project Description 2'
    },
    {
        'id': 3,
        'title': 'Project 3',
        'description': 'Project Description 3'
    }
]

tasks = [
    {
        'id': 1,
        'project_id': 1,
        'title': 'Task 1 - Project 1',
        'description': 'This is the first task for Project 1'
    },
    {
        'id': 2,
        'project_id': 1,
        'title': 'Task 2 - Project 1',
        'description': 'This is the second task for Project 1'
    },
    {
        'id': 3,
        'project_id': 2,
        'title': 'Task 3 - Project 2',
        'description': 'This is the only task for Project 2'
    }
]

# --- Projects Endpoints ---

@app.route('/projects', methods=['GET'])
def get_projects():
    return jsonify(projects)
    
@app.route('/projects/<int:id>', methods=['GET'])
def get_project_by_id(id):
    for project in projects:
        if project.get('id') == id:
            return jsonify(project)
    return jsonify({'message': 'Project not found'}), 404

@app.route('/projects/<int:id>', methods=['PUT'])
def edit_project_by_id(id):
    project_changed = request.get_json()
    for index, project in enumerate(projects):
        if project.get('id') == id:
            projects[index].update(project_changed)
            print(f'Project {project.get("id")} changed successfully!')
            return jsonify(projects[index])
    return jsonify({'message': 'Project not found'}), 404

@app.route('/projects', methods=['POST'])
def create_project():
    new_project = request.get_json()
    projects.append(new_project)
    print(f'Project {new_project.get("id")} created successfully!')
    return jsonify(new_project), 201

@app.route('/projects/<int:id>', methods=['DELETE'])
def delete_project_by_id(id):
    for index, project in enumerate(projects):
        if project.get('id') == id:
            del projects[index]
            print(f'Project {project.get("id")} deleted successfully!')
            return jsonify({'message': 'Project deleted successfully!'}), 204
    return jsonify({'message': 'Project not found'}), 404

# --- Tasks Endpoints ---

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/projects/<int:project_id>/tasks', methods=['GET'])
def get_tasks_by_project_id(project_id):
    project_tasks = [task for task in tasks if task.get('project_id') == project_id]
    return jsonify(project_tasks)

@app.route('/projects/<int:project_id>/tasks', methods=['POST'])
def create_task(project_id):
    new_task = request.get_json()
    new_task['project_id'] = project_id
    tasks.append(new_task)
    return jsonify(new_task), 201
    
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task_by_id(id):
    for task in tasks:
        if task.get('id') == id:
            return jsonify(task)
    return jsonify({'message': 'Task not found'}), 404

@app.route('/tasks/<int:id>', methods=['PUT'])
def edit_task_by_id(id):
    task_changed = request.get_json()
    for index, task in enumerate(tasks):
        if task.get('id') == id:
            tasks[index].update(task_changed)
            return jsonify(tasks[index])
    return jsonify({'message': 'Task not found'}), 404

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task_by_id(id):
    for index, task in enumerate(tasks):
        if task.get('id') == id:
            del tasks[index]
            return jsonify({'message': 'Task deleted successfully!'}), 204
    return jsonify({'message': 'Task not found'}), 404

app.run(port=5000, host='localhost', debug=True)