from lib.task_list import TaskList

"""
Initially,
The incomplete tasks list is empty
"""
def test_initially_incomplete_is_empty():
    task_list = TaskList()
    assert task_list.list_incomplete() == []

"""
Initially,
The complete tasks list is empty
"""
def test_initially_complete_is_empty():
    task_list = TaskList()
    assert task_list.list_complete() == []
