import json
from datetime import datetime

from flask import Flask, jsonify, redirect, render_template, request, session, url_for

# Create Flask app
app = Flask(__name__)
app.secret_key = "your-secret-key-here"  # Needed for sessions

# In-memory data storage (use database in production)
users = []
posts = []


# Home page
@app.route("/")
def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <h1>Welcome to My Flask App</h1>
    <p>Current time: {current_time}</p>
    <ul>
        <li><a href="/users">View Users</a></li>
        <li><a href="/posts">View Posts</a></li>
        <li><a href="/add-user">Add User</a></li>
        <li><a href="/api/users">API: Get Users (JSON)</a></li>
    </ul>
    """


# Display users
@app.route("/users")
def show_users():
    if not users:
        return '<h2>No users found</h2><a href="/add-user">Add a user</a>'

    html = "<h2>Users List</h2><ul>"
    for user in users:
        html += f'<li><strong>{user["name"]}</strong> ({user["email"]}) - Age: {user["age"]}</li>'
    html += '</ul><a href="/add-user">Add another user</a>'
    return html


# Form to add user (GET shows form, POST processes it)
@app.route("/add-user", methods=["GET", "POST"])
def add_user():
    if request.method == "GET":
        return """
        <h2>Add New User</h2>
        <form method="POST">
            <p>Name: <input type="text" name="name" required></p>
            <p>Email: <input type="email" name="email" required></p>
            <p>Age: <input type="number" name="age" required></p>
            <p><input type="submit" value="Add User"></p>
        </form>
        <a href="/">Back to Home</a>
        """

    # POST request - process form data
    name = request.form["name"]
    email = request.form["email"]
    age = int(request.form["age"])

    # Add user to our list
    users.append(
        {
            "id": len(users) + 1,
            "name": name,
            "email": email,
            "age": age,
            "created_at": datetime.now().isoformat(),
        }
    )

    # Redirect to users page
    return redirect(url_for("show_users"))


# API endpoint - return JSON
@app.route("/api/users")
def api_users():
    return jsonify(
        {"users": users, "total": len(users), "timestamp": datetime.now().isoformat()}
    )


# API endpoint - get specific user
@app.route("/api/users/<int:user_id>")
def api_get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


# API endpoint - create user with JSON
@app.route("/api/users", methods=["POST"])
def api_create_user():
    data = request.json
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Name and email required"}), 400

    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "email": data["email"],
        "age": data.get("age", 0),
        "created_at": datetime.now().isoformat(),
    }

    users.append(new_user)
    return jsonify(new_user), 201


# URL with parameters
@app.route("/user/<name>")
def user_profile(name):
    user = next((u for u in users if u["name"].lower() == name.lower()), None)
    if user:
        return f"""
        <h2>User Profile: {user["name"]}</h2>
        <p>Email: {user["email"]}</p>
        <p>Age: {user["age"]}</p>
        <p>Created: {user["created_at"]}</p>
        <a href="/users">Back to Users</a>
        """
    return f'<h2>User "{name}" not found</h2><a href="/users">Back to Users</a>', 404


# Simple blog posts
@app.route("/posts")
def show_posts():
    if not posts:
        return '<h2>No posts yet</h2><a href="/create-post">Create first post</a>'

    html = "<h2>Blog Posts</h2>"
    for post in posts:
        html += f"""
        <div style="border: 1px solid #ccc; margin: 10px; padding: 10px;">
            <h3>{post["title"]}</h3>
            <p>{post["content"]}</p>
            <small>By: {post["author"]} | {post["created_at"]}</small>
        </div>
        """
    html += '<a href="/create-post">Create new post</a>'
    return html


@app.route("/create-post", methods=["GET", "POST"])
def create_post():
    if request.method == "GET":
        return """
        <h2>Create New Post</h2>
        <form method="POST">
            <p>Title: <input type="text" name="title" required style="width: 300px;"></p>
            <p>Author: <input type="text" name="author" required></p>
            <p>Content:<br><textarea name="content" rows="5" cols="50" required></textarea></p>
            <p><input type="submit" value="Create Post"></p>
        </form>
        <a href="/posts">Back to Posts</a>
        """

    # Create new post
    posts.append(
        {
            "id": len(posts) + 1,
            "title": request.form["title"],
            "content": request.form["content"],
            "author": request.form["author"],
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
    )

    return redirect(url_for("show_posts"))


# Error handler
@app.errorhandler(404)
def not_found(error):
    return (
        """
    <h2>404 - Page Not Found</h2>
    <p>The page you're looking for doesn't exist.</p>
    <a href="/">Go to Home</a>
    """,
        404,
    )


# Run the app
if __name__ == "__main__":
    app.run(debug=True, port=5000)
