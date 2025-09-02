from datetime import datetime
import uuid

class Task:
    def __init__(self, project_id: str, title: str, assigned_to: str, description: str, status: str = "a_fazer", due_date: str = None):
        self.id = str(uuid.uuid4())
        self.project_id = project_id
        self.title = title
        self.description = description
        self.status = status
        self.due_date = due_date
        self.assigned_to = assigned_to
        self.created_at = datetime.now().isoformat()
    
    def to_dict(self):
        return {
            "id": self.id,
            "projectId": self.project_id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "dueDate": self.due_date,
            "assignedTo": self.assigned_to,
            "createdAt": self.created_at
        }