import json, sys, os
from json.decoder import JSONDecodeError
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
def update_task(task_id, task_name):
    for task in tasks_list:
        if int(task.get("id")) == int(task_id):
            task["data"]["description"] = task_name
            task["data"]["updatedAt"] = datetime.now().strftime(date_format)
    return
def delete_task(task_id):
    for task in tasks_list:
        if int(task.get("id")) == int(task_id):
            tasks_list.remove(task)
            # do not change id values atm
            return
def mark_task(mark_type, task_id):
    return

command = sys.argv[1] 
if not os.path.exists("tasks.json"):
    with open('tasks.json', 'w') as tasks_file:
        json.dump([], tasks_file)
with open('tasks.json', 'r') as tasks_file:
    tasks_list=json.load(tasks_file)
with open('tasks.json', 'w') as tasks_file: 
    match command:
        case 'add':
            tasks_list = add_task(sys.argv[2])
        case 'update':
            update_task(sys.argv[2], sys.argv[3])
        case 'delete':
            delete_task(sys.argv[2])
        case 'mark-in-progress' | 'mark-done':
            mark_task(sys.argv[2], sys.argv[3])
        case 'list':    
            for task in tasks_list:
                pprint(task, sort_dicts=False)
    json.dump(tasks_list, tasks_file, indent=4)
# json.dump(task_dict, tasks_json)