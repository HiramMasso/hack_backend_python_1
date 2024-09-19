from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

#hack1
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'payload': 'success'})

#hack2
@app.route('/user', methods=['POST'])
def get_user():
    return jsonify({'payload': 'success'})

#hack3
@app.route('/user', methods=['DELETE'])
def get_user1():
    return jsonify({'payload': 'success'})

#hack4
@app.route('/user', methods=['PUT'])
def get_user2():
    return jsonify({'payload': 'success', 'error': False})

#hack5
@app.route('/api/v1/users', methods=['GET'])
def get_api1():
    return jsonify({'payload': []})

#hack6
@app.route('/api/v1/user', methods=['POST'])
def get_api2():
    email = request.args.get('email')
    name = request.args.get('name')
    return jsonify({'payload': {'email': email, 'name': name}})

#hack7
@app.route('/api/v1/user/add', methods=['POST'])
def get_api3():
    email = request.form.get('email')
    name = request.form.get('name')
    user_id = request.form.get('id')
    return jsonify({'payload': {'email': email, 'name': name, 'id': user_id}})

#hack8
@app.route('/api/v1/user/create', methods=['POST'])
def create_user():
    data = request.get_json()
    email = data.get('email')
    name = data.get('name')
    user_id = data.get('id')
    return jsonify({'payload': {'email': email,'name': name,'id': user_id}})

if __name__ == "__main__":
    app.run(debug=True)