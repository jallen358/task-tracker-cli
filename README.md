### Task Tracking CLI App
---
This is a task tracker built in python using os, sys, and json libraries. 

To run, open terminal in the folder and use following commands:
To add a task:
```bash
task-cli.py add "Name/Description of task"
```
Tasks are automatically marked as TODO

To update a task:
```bash
task-cli.py update 1 "New Name/Description of task"
```

To delete a task:
```bash
task-cli.py delete 1
```

To change the status of a task:
```bash
task-cli.py mark-in-progress 1
```
Only in-progress, todo, and done are supported status currently

To list tasks:
```
task-cli.py list
task-cli.py list in-progress
task-cli.py list todo
task-cli.py list done
```
