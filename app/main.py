from flask import Flask
from app.controllers.project_controller import project_bp
from app.controllers.task_controller import task_bp

app = Flask(__name__)

app.register_blueprint(project_bp, url_prefix='/api/v1/projects')
app.register_blueprint(task_bp, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run(debug=True)