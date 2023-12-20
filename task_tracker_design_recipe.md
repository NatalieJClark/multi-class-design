# {{Task Tracker}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
# Nouns - Things the user will interact with
task
list of tasks
(program)

# Verbs - Operations that the user is going to perform
add
see a list
mark complete
disappear


  ┌────────────────────────────────┐
  │                                │
  │ TaskList                       │
  │                                │
  │ - add(task)                    │
  │ - list_incomplete()            │
  │ - list_complete()              │
  │                                │
  │                                │
  └───────────────┬────────────────┘
                  │
                  │
                  │
                  ▼
  ┌────────────────────────────────┐
  │                                │
  │ Task                           │
  │                                │
  │ - initialise(title)            │
  │ - mark complete()              │
  │ - complete [property]          │
  │                                │
  │                                │
  │                                │
  └────────────────────────────────┘


```

_Also design the interface of each class in more detail._

```python

class TaskList()
    def add(self, task):
        # Parameters:
        #   task: an instance of the Task class
        # Side effect:
        #   adds task to an internal list of tasks
        pass

    def list_incomplete(self):
        # Returns:
        #   A list of instances of Task that are incomplete
        pass
    
    def list_complete(self):
        # Returns:
        #   A list of instances of Task that are complete
        pass

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
        pass

    def mark_complete(self):
        # Side-effects:
        #   Marks the task as complete
        pass
```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python

"""
When I add multiple tasks
They come back in the incomplete list
"""
task_list = TaskList()
task_1 = Task("Walk the dog")
task_2 = Task("Walk the cat")
task_list.add(task_1)
task_list.add(task_2)
task_list.list_incomplete() #=> [task_1, task_2]

"""
When I add multiple tasks
And mark one as complete
It dosen't show in the incomplete list anymore
"""
task_list = TaskList()
task_1 = Task("Walk the dog")
task_2 = Task("Walk the cat")
task_list.add(task_1)
task_list.add(task_2)
task_1.mark_complete()
task_list.list_incomplete() #=> [task_2]

"""
When I add multiple tasks
And mark one as complete
It show in the complete list
"""
task_list = TaskList()
task_1 = Task("Walk the dog")
task_2 = Task("Walk the cat")
task_list.add(task_1)
task_list.add(task_2)
task_1.mark_complete()
task_list.list_complete() #=> [task_1]

```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python

# TaskList unit tests
"""
Initially,
The incomplete tasks list is empty
"""
task_list = TaskList()
task_list.list_incomplete() #=> []

"""
Initially,
The complete tasks list is empty
"""
task_list = TaskList()
task_list.list_complete() #=> []

# Task unit tests
"""
When we construct with a title
We get that title reflected back in the title property
"""
task = Task("Walk the dog")
task.title #=> "Walk the dog"

"""
When we construct
The task is initially incomplete
"""
task = Task("Walk the dog")
task.complete #=> False

"""
When we mark a task as complete
It is reflected in the complete property
"""
task = Task("Walk the dog")
task.mark_complete()
task.complete #=> True

```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._

