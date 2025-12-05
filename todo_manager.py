import pickle
import time
import threading
from task import Task

class TodoManager:
    def __init__(self):
        self.tasks = []
        self.lock = threading.Lock()
        self.load()

    def load(self):
        try:
            with open("tasks.dat", "rb") as f:
                self.tasks = pickle.load(f)
        except:
            self.tasks = []

    def save(self):
        with open("tasks.dat", "wb") as f:
            pickle.dump(self.tasks, f)

    def add_task(self, title, category, priority, deadline):
        t = Task(title, category, priority, deadline)
        with self.lock:
            self.tasks.append(t)
        self.save()
        self.start_reminder(t)

    def start_reminder(self, task):
        if task.deadline:
            def wait_and_alert():
                now = time.time()
                if task.deadline > now:
                    time.sleep(task.deadline - now)
                if not task.completed:
                    print("\n[ALERT] Deadline reached for:", task.title)
            th = threading.Thread(target=wait_and_alert, daemon=True)
            th.start()

    def delete_task(self, index):
        with self.lock:
            if 0 <= index < len(self.tasks):
                self.tasks.pop(index)
        self.save()

    def mark_done(self, index):
        with self.lock:
            if 0 <= index < len(self.tasks):
                self.tasks[index].completed = True
        self.save()

    def search(self, keyword):
        return [t for t in self.tasks if keyword.lower() in t.title.lower() or keyword.lower() in t.category.lower()]
