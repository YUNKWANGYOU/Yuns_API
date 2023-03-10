
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}

class TodoSimple(Resource):

    #curl http://localhost:5000/todo_1
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    #curl http://localhost:5000/todo_1 -d "data=go to shower" -X PUT
    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=False)