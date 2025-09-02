from datetime import datetime
import uuid

class Project:
    def __init__(self, title: str, description: str, status: str = "ativo"):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.status = status
        self.created_at = datetime.now().isoformat()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "createdAt": self.created_at
        }