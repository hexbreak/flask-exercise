from flask import Flask, jsonify, request
import json
app = Flask(__name__)

# for learning purposes, not to use on real projects on line 8!
# import jsonify to work

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json() #replaced request.data with get_json()
    print("Incoming request with the following body", request_body)
    # decoded_object = json.loads(original_string)
    todos.append(request_body)
    return jsonify(todos), 200

# we can skip json load because it comes from the request itself on flasks import get_json() works better.

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    removed = todos.pop(position)
    result = { "newList": todos, "erasedList": removed }
    return jsonify(result), 200

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)