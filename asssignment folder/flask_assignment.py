from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)

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

#http://127.0.0.1:5000/
@app.route('/')
def hello_world():
	return 'Hello, world!'


# #http://127.0.0.1:5000/users?name=Mac
# @app.route('/users')
# def get_users():
#    search_username = request.args.get('name') # accessing the value of parameter 'name'
#    if search_username:
#       subdict = {'users_list' : []}
#       for user in users['users_list']:
#          if user['name'] == search_username:
#             subdict['users_list'].append(user)
#       return subdict
#    return users


#http://127.0.0.1:5000/users/zap555
@app.route('/users/<id>')
def get_user(id):
   if id :
      for user in users['users_list']:
        if user['id'] == id:
           return user
      return ({})
   return users


#POST / GETTER
#http://127.0.0.1:5000/users?name=Dennis&job=Bartender
@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
   if request.method == 'GET':

      search_username = request.args.get('name')
      if search_username :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username:
               subdict['users_list'].append(user)
         return subdict

      search_job = request.args.get('job')
      if search_username and search_job :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username and user['job'] == search_job:
               subdict['users_list'].append(user)
         return subdict

      return users

   elif request.method == 'DELETE':

       search_username = request.args.get('name')
       if search_username :
         count = 0
         for user in users['users_list']:
            if user['name'] == search_username:
               users['users_list'].pop(count)
               return users
            count += 1
         return users

   elif request.method == 'POST':
      userToAdd = request.get_json()
      users['users_list'].append(userToAdd)
      resp = jsonify(success=True)
      #resp.status_code = 200 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp