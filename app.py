from flask import Flask, request, jsonify
# from math import Math
import random
import time

app = Flask(__name__)

# id, title, description, status, created_at, updated_at

task_list = []

def generateRandomNumber():
  num = time.time() * 1000
  return num

def getTaskByID():

  return

def putTaskById(title, derscription, ):
  
  return

def addNewTask(title, description, created_at, updated_at, updated_by = 'guest'):
  task = {
    'id': generateRandomNumber(), #Math.random()
    'title': title, 
    'description': description, 
    'status': 'ACTIVE', #ACTIVE/INACTIVE
    'created_at': created_at, #DATETIME
    'updated_at': updated_at, #DATETIME
    'updated_by': updated_by
  }

  task_list.append(task)
  return

def deleteTaskById():

  return


@app.route('/tasks', methods=['GET', 'POST'])
def all_tasks():
  if(request.method == 'GET'):
    return jsonify(task_list)

  elif(request.method == 'POST'):
    title = request.form['title']
    description =  request.form['description']
    created_at =  request.form['created_at']
    updated_at =  request.form['updated_at']
    updated_by =  request.form['updated_by']

    addNewTask(title, description, created_at, updated_at, updated_by)

  return

@app.route('/tasks/<id>', methods=['GET', 'PUT', 'DELETE'])
def task_by_id():
  if(request.method == 'GET'):
    getTaskByID()

  elif(request.method == 'PUT'):
    putTaskById()

  elif(request.method == 'DELETE'):
    deleteTaskById()

  return


@app.route('/tasks/<id>')
def task_by_id():
  return


if __name__=='__main__':
  app.run(debug=True)