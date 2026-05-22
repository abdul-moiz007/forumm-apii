from flask import Blueprint, jsonify, request
from data.db import posts

posts_bp = Blueprint('posts', __name__)

# GET all posts
@posts_bp.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

# GET single post
@posts_bp.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    for post in posts:
        if post["id"] == id:
            return jsonify(post)
    return jsonify({"error": "Post not found"}), 404

# CREATE post
@posts_bp.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    new_post = {
        "id": len(posts) + 1,
        "title": data["title"],
        "content": data["content"]
    }
    posts.append(new_post)
    return jsonify(new_post), 201

# UPDATE post
@posts_bp.route('/posts/<int:id>', methods=['PUT'])
def update_post(id):
    for post in posts:
        if post["id"] == id:
            data = request.get_json()
            post["title"] = data.get("title", post["title"])
            post["content"] = data.get("content", post["content"])
            return jsonify(post)
    return jsonify({"error": "Post not found"}), 404

# DELETE post
@posts_bp.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    for post in posts:
        if post["id"] == id:
            posts.remove(post)
            return jsonify({"message": "Deleted successfully"})
    return jsonify({"error": "Post not found"}), 404