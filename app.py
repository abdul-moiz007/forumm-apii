# Import required libraries
from flask import Flask, jsonify, request

# Create Flask app
app = Flask(__name__)


# Fake Database (In-Memory Storage)

# This list stores all posts temporarily
posts = [
    {"id": 1, "title": "First Post", "content": "Hello World"},
    {"id": 2, "title": "Second Post", "content": "Learning Flask"},
    {"id": 3, "title": "Third Post", "content": "Building APIs"},
    {"id": 4, "title": "Fourth Post", "content": "Python is great!"},
    {"id": 5, "title": "Fifth Post", "content": "Flask is lightweight"},
    {"id": 6, "title": "Sixth Post", "content": "APIs are fun"},
    {"id": 7, "title": "Seventh Post", "content": "Testing is important"},
    {"id": 8, "title": "Eighth Post", "content": "Deployment is key"},
    {"id": 9, "title": "Ninth Post", "content": "Keep coding!"},
    {"id": 10, "title": "Tenth Post", "content": "Happy coding!"}

]


# HOME ROUTE (Fixes 404 error)

@app.route('/')
def home():
    return "Forum API is running 🚀"


# GET ALL POSTS
# URL: /posts
# METHOD: GET

@app.route('/posts', methods=['GET'])
def get_posts():
    # Return all posts as JSON
    return jsonify(posts)


# GET SINGLE POST
# URL: /posts/<id>
# METHOD: GET

@app.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    # Loop through posts to find matching id
    for post in posts:
        if post["id"] == id:
            return jsonify(post)
    
    # If not found
    return jsonify({"error": "Post not found"}), 404


# CREATE NEW POST
# URL: /posts
# METHOD: POST

@app.route('/posts', methods=['POST'])
def create_post():
    # Get JSON data from request body
    data = request.get_json()

    # Create new post dictionary
    new_post = {
        "id": len(posts) + 1,   # Auto increment ID
        "title": data["title"],
        "content": data["content"]
    }

    # Add new post to list
    posts.append(new_post)

    # Return created post with status 201
    return jsonify(new_post), 201

# UPDATE EXISTING POST
# URL: /posts/<id>
# METHOD: PUT

@app.route('/posts/<int:id>', methods=['PUT'])
def update_post(id):
    # Loop to find post
    for post in posts:
        if post["id"] == id:
            # Get updated data
            data = request.get_json()

            # Update values if provided
            post["title"] = data.get("title", post["title"])
            post["content"] = data.get("content", post["content"])

            return jsonify(post)

    return jsonify({"error": "Post not found"}), 404


# DELETE POST
# URL: /posts/<id>
# METHOD: DELETE

@app.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    # Find and delete post
    for post in posts:
        if post["id"] == id:
            posts.remove(post)
            return jsonify({"message": "Post deleted successfully"})

    return jsonify({"error": "Post not found"}), 404


# RUN SERVER

if __name__ == '__main__':
    app.run(debug=True)