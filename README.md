# Multi Class Task Tracker

## Introduction
- This is my repo for Makers Module 2 - Golden Square: Designing a Multi Class System
- This project was an exercise for this module section
- The `task_tracker_design_recipe.md` documents my design of the class system and tests based on the user stories
- This project contains a Task class and a TaskList class, as well as unit and integration tests
- The user can create Task objects and add them to a TaskList object
- The user can also:
  - mark a Task object complete
  - list all the complete Task instances in a TaskList object
  - list all the incomplete Task instances in a TaskList object
  
## Objectives
I used this project to:
- [x] Learn to design a multi-class program
- [x] Consolidate my knowledge of encapsulating state and behaviour as classes
- [x] Consolidate my knowledge of writing unit and integration tests for a multi-class program  

## Setup
This project uses `python`, `pyenv` and `pipenv`. Here's how to install it:

```shell
# Install pyenv, a tool to manage different versions of Python.
# This will ensure you have the latest Python, which has more readable error messages.
; brew install pyenv
# You may be given some extra instructions at the end of the command.
# If you are, follow them. If not, keep going.

# Now install the latest Python.
; pyenv install 3.11

# Install pipenv
; python3 -m ensurepip --upgrade
; pip3 install --user pipenv
; echo 'export PATH="$PATH:$(python3 -m site --user-base)/bin" # Add Pipenv to PATH' >> ~/.zshrc
; source ~/.zshrc
; pipenv --version # Check pipenv is installed
pipenv, version ...
```
To test the practise code: 
```shell
# Install the dependencies (pytest)
; pipenv install # NB: you may need to change interpreters to import pytest

# Optionally ...
# Activate the project's virtualenv
; pipenv shell

# If using the pipenv shell:
# This runs all of the tests in the current directory
; pytest
# And this exits the pipenv shell
; exit # or Ctrl-D

# Otherwise, this runs all of the tests in the current directory
; pipenv run pytest
```
