#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Flask API!"


users = {

}

@app.route("/data")
def get_usernames():
    username = list(users.keys())
    return jsonify(username)

@app.route("/status")
def stats():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    infouser = users.get(username)
    if infouser is None:
        return {"error": "User not found"}
    return jsonify(infouser)

@app.route("/add_user", methods=["POST"])
def post_user():
    create = request.get_json()
    new_user = create.get('username')
    new_name = create['name']
    new_age = create['age']
    new_city = create['city']

    if not isinstance(new_user, str) or users:
        return jsonify({"error": "Username is required"}), 400
    

    users[new_user] = {"username": new_user, "name": new_name, "age": new_age, "city": new_city}

    message = {"message": "user added", "user": users[new_user]}
    return jsonify(message)

if __name__ == "__main__":
    app.run()