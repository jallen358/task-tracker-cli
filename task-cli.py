import json, sys, os
from datetime import datetime
from pprint import pprint

"""
JSON which holds the tasks

{
id : {
 description,
 status,
 createdAt,
 updatedAt
    }
 }
"""

date_format = "%Y/%m/%d %H:%M:%S"

# Adding a task to the JSON
def add_task(task_name):
    if tasks_list:
        next_id = max(item["id"] for item in tasks_list)
    else: 
        next_id = 0
    task = {
        "id" : next_id + 1,
        "data":{
            "description": task_name,
            "status": '',
            "createdAt": datetime.now().strftime(date_format),
            "updatedAt": datetime.now().strftime(date_format)
        }
    }
    tasks_list.append(task)
    return tasks_list
# Updating the description of a task in the JSON
def update_task(task_id, task_name):
    for task in tasks_list:
        if int(task.get("id")) == int(task_id):
            task["data"]["description"] = task_name
            task["data"]["updatedAt"] = datetime.now().strftime(date_format)
    return

# Deleting a task
def delete_task(task_id):
    for task in tasks_list:
        if int(task.get("id")) == int(task_id):
            tasks_list.remove(task)
            return
        
# Marking status of a task
def mark_task(mark_type, task_id):
    mark_type = mark_type[5:]
    for task in tasks_list:
        if int(task.get("id")) == int(task_id):
            task["data"]["status"] = mark_type
            task["data"]["updatedAt"] = datetime.now().strftime(date_format)
    return

# listing all tasks
def list_tasks(task_status):
    for task in tasks_list:
        if task.get("data")["status"] == task_status:
            pprint(task, sort_dicts=False)

command = sys.argv[1] 
if not os.path.exists("tasks.json") or os.path.getsize("tasks.json") == 0:
    with open('tasks.json', 'w') as tasks_file:
        json.dump([], tasks_file)
with open('tasks.json', 'r') as tasks_file:
    tasks_list=json.load(tasks_file)

# Main running loop
with open('tasks.json', 'w') as tasks_file: 
    match command:
        case 'add':
            tasks_list = add_task(sys.argv[2])
        case 'update':
            update_task(sys.argv[2], sys.argv[3])
        case 'delete':
            delete_task(sys.argv[2])
        case 'mark-in-progress' | 'mark-done' | 'mark-todo':
            mark_task(sys.argv[1], sys.argv[2])
        case 'list': 
            if len(sys.argv) == 2:   
                for task in tasks_list:
                    pprint(task, sort_dicts=False)
            else:
                list_tasks(sys.argv[2])
    json.dump(tasks_list, tasks_file, indent=4)
