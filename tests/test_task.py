from lib.task import Task

"""
When we construct with a title
We get that title reflected back in the title property
"""
def test_constructs_with_a_title():
    task = Task("Walk the dog")
    assert task.title == "Walk the dog"

"""
When we construct
The task is initially incomplete
"""
def test_task_is_initially_incomplete():
    task = Task("Walk the dog")
    assert task.complete == False

"""
When we mark a task as complete
It is reflected in the complete property
"""
def test_marks_complete():
    task = Task("Walk the dog")
    task.mark_complete()
    assert task.complete == True
