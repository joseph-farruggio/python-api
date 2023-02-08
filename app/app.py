import json

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/user/*": {"origins": "*"}})

@app.route('/user/<username>')
def get_user(username):
    with open('users.json') as f:
        users = json.load(f)

    user = next((user for user in users if user['username'] == username), None)

    if user:
        return jsonify(user)
    else:
        return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)