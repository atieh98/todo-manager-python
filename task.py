class Task:
    def __init__(self, title, category, priority, deadline=None):
        self.title = title
        self.category = category
        self.priority = priority
        self.deadline = deadline
        self.completed = False
        self.cancelled = False

    def to_dict(self):
        return {
            "title": self.title,
            "category": self.category,
            "priority": self.priority,
            "deadline": self.deadline,
            "completed": self.completed,
        }
