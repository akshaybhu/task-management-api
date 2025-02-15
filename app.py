from flask import Flask, request, jsonify # type: ignore
import random, time

app = Flask(__name__)

# id, title, description, status, created_at, updated_at

task_list = []
task_list_byID = []
required_fields = ['title', 'description']

def generateRandomNumber():
  num = time.time_ns()
  return num


def getTaskByID(id):
  for t in task_list:
	  if t['id'] == int(id):
		  return t


def putTaskById(id, title, description, updated_by):
  # title = request.form['title']
  # description =  request.form['description']
  # updated_by =  request.form['updated_by']
  
  if int(id) in task_list_byID:
    for task in task_list:
      if int(id) == task['id']:
        task['title'] = title
        task['description'] = description
        task['updated_by'] = updated_by
        task['updated_at'] = time.time_ns()
        return True
  else:
    return False


def addNewTask(title, description, created_at, updated_by = 'guest'):
  task = {
    'id': generateRandomNumber(), #Math.random()
    'title': title, 
    'description': description, 
    'status': 'ACTIVE', #ACTIVE/INACTIVE
    'created_at': created_at, #DATETIME
    'updated_at': created_at, #DATETIME
    'updated_by': updated_by
  }

  task_list.append(task)
  #print(task_list)
  task_list_byID.append(task['id'])


def deleteTaskById(id):
  if int(id) in task_list_byID:
    for index, task in enumerate(task_list):
      print(task, index)
      if int(id) == task['id']:
        task_list.pop(index)
        task_list_byID.remove(int(id))
        return True
  else:
     return False


@app.route('/tasks', methods=['GET', 'POST'])
def all_tasks():
  if(request.method == 'GET'):
    return jsonify(task_list)

  elif(request.method == 'POST'):
    body = request.json
    created_at =  time.time_ns()
    if not all(field in body for field in required_fields):
      return jsonify('Title and Description are mandatory.')
    
    title = body['title']
    description =  body['description']
    updated_by =  body.get('updated_by', 'guest')
    addNewTask(title, description, created_at, updated_by)
    return jsonify('Added successfully')

@app.route('/tasks/<id>', methods=['GET', 'PUT', 'DELETE'])
def task_by_id(id):
  if(request.method == 'GET'):
    tsk = getTaskByID(id)
    if tsk:
      return jsonify(tsk)
    else:
       return "No such ID found"
       

  elif(request.method == 'PUT'):
    body = request.json
    if not all(field in body for field in required_fields):
      return jsonify('Title and Description are mandatory.')
    
    title = body['title']
    description =  body['description']
    # updated_by = body['updated_by']
    updated_by =  body.get('updated_by', 'guest')

    updated_recall = putTaskById(id, title, description, updated_by)
    if updated_recall:
       return "Updated Successfully"
    else:
       return "No such ID found"

  elif(request.method == 'DELETE'):
    updated_recall = deleteTaskById(id)
    if updated_recall:
      return "Deleted Successfully"
    else:
      return "No such ID found"


if __name__=='__main__':
  app.run(debug=True)