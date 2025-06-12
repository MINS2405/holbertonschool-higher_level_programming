from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user storage
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    # Return the list of usernames
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    # Build the user object from the incoming data
    user_obj = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", ""),
        "city": data.get("city", "")
    }
    users[username] = user_obj
    return jsonify({
        "message": "User added",
        "user": user_obj
    }), 201

if __name__ == "__main__":
    app.run()
