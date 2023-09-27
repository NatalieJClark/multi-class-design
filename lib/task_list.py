class TaskList():
    def __init__(self):
        self._tasks = []

    def add(self, task):
        # Parameters:
        #   task: an instance of the Task class
        # Side effect:
        #   adds task to an internal list of tasks
        self._tasks.append(task)

    def list_incomplete(self):
        # Returns:
        #   A list of instances of Task that are incomplete
        return [
            task for task in self._tasks
            if not task.complete
        ]
    
    def list_complete(self):
        # Returns:
        #   A list of instances of Task that are complete
        return [
            task for task in self._tasks
            if task.complete
        ]