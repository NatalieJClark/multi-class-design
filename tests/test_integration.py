from lib.task_list import TaskList
from lib.task import Task

"""
When I add multiple tasks
They come back in the incomplete list
"""
def test_adds_and_lists_incomplete_tasks():
    task_list = TaskList()
    task_1 = Task("Walk the dog")
    task_2 = Task("Walk the cat")
    task_list.add(task_1)
    task_list.add(task_2)
    assert task_list.list_incomplete() == [task_1, task_2]

"""
When I add multiple tasks
And mark one as complete
It doesn't show in the incomplete list anymore
"""
def test_marks_tasks_as_complete_and_removes_them_from_incomplete():
    task_list = TaskList()
    task_1 = Task("Walk the dog")
    task_2 = Task("Walk the cat")
    task_list.add(task_1)
    task_list.add(task_2)
    task_1.mark_complete()
    assert task_list.list_incomplete() == [task_2]

"""
When I add multiple tasks
And mark one as complete
It show in the complete list
"""
def test_marks_complete_and_adds_to_complete_list():
    task_list = TaskList()
    task_1 = Task("Walk the dog")
    task_2 = Task("Walk the cat")
    task_list.add(task_1)
    task_list.add(task_2)
    task_1.mark_complete()
    assert task_list.list_complete() == [task_1]
