class Task():
    # Public properties:
    #   title: a string representing a task to do
    #   complete: a boolean, True if task is complete, False otherwise
    def __init__(self, title):
        # Parameters:
        #   title: a string representing a task to do
        # Side__effects:
        #   Sets the title property
        #   Sets the complete property as False, at first
        self.title = title
        self.complete = False

    def mark_complete(self):
        # Side-effects:
        #   Marks the task as complete
        self.complete = True