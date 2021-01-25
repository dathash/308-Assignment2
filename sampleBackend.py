from flask import Flask, request, jsonify
from flask_cors import CORS
import random
app = Flask(__name__)
CORS(app)

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

@app.route('/users', methods=["GET", "POST"])
def get_users():
    if request.method == "GET":
        search_username = request.args.get('name')
        search_job = request.args.get('job')
        if search_username:
            subdict = {'users_list':[]}
            for user in users['users_list']:
                if user['name'] == search_username:
                    if search_job:
                        if user['job'] == search_job:
                            subdict['users_list'].append(user)
                    else:
                        subdict['users_list'].append(user)
            return subdict
        return users
    elif request.method == "POST":
        userToAdd = request.get_json()
        userToAdd['id'] = generate_id()
        users['users_list'].append(userToAdd)
        resp = jsonify(userToAdd)
        resp.status_code = 201
        return resp

def generate_id():
    new_id = ""
    new_id = (new_id + chr(97+random.randrange(26))
                     + chr(97+random.randrange(26))
                     + chr(97+random.randrange(26)))
    new_id = (new_id + str(random.randrange(9)) + 
                       str(random.randrange(9)) + 
                       str(random.randrange(9)))
    return new_id

@app.route('/users/<id>', methods=["GET", "DELETE"])
def get_user(id):
    if request.method == "GET":
        if id:
            for user in users['users_list']:
                if user['id'] == id:
                    return user
            return ({})
        return users
    elif request.method == "DELETE":
        if id:
            for user in users['users_list']:
                if user['id'] == id:
                    users['users_list'].remove(user)
                    resp = jsonify(success=True)
                    resp.status_code = 204
                    return resp
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp

@app.route('/')
def hello_world():
    return "Hello, World!"