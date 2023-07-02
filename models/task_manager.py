# Import necessary modules
import threading
import time

class Task:
    def __init__(self, task_id, task_name, priority=0, args=None):
        self.task_id = task_id
        self.task_name = task_name
        self.priority = priority
        self.args = args

class TaskManager:
    def __init__(self):
        self.task_queue = []
        self.is_running = False

    def add_task(self, task):
        self.task_queue.append(task)
        self.task_queue.sort(key=lambda x: x.priority, reverse=True)

    def execute_task(self, task):
        # Perform the task execution logic here based on the task_name and args
        print(f"Executing task: {task.task_name}")
        time.sleep(2)  # Simulating task execution time

    def process_tasks(self):
        while self.is_running:
            if not self.task_queue:
                time.sleep(1)
                continue

            task = self.task_queue.pop(0)
            self.execute_task(task)

    def start(self):
        self.is_running = True
        task_thread = threading.Thread(target=self.process_tasks)
        task_thread.start()

    def stop(self):
        self.is_running = False

if __name__ == "__main__":
    # Sample usage of TaskManager
    task_manager = TaskManager()
    task_manager.start()

    # Add tasks to the queue
    task_manager.add_task(Task(task_id=1, task_name="Task 1", priority=1, args={"param1": "value1"}))
    task_manager.add_task(Task(task_id=2, task_name="Task 2", priority=2, args={"param2": "value2"}))
    task_manager.add_task(Task(task_id=3, task_name="Task 3", priority=0, args={"param3": "value3"}))

    # Let the tasks execute
    time.sleep(5)

    # Stop the task manager
    task_manager.stop()
