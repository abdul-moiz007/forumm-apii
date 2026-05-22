# Forum API Project

A complete RESTful API for managing forum posts, built with Python and Flask. This project demonstrates all CRUD operations (Create, Read, Update, Delete) and is ideal for learning, practice, or as a report submission.

---

## Table of Contents
1. [What is a REST API?]
2. [Project Structure]
3. [Setup Instructions]
4. [Running the API]
5. [API Endpoints & Usage]
6. [How the Code Works]
7. [Extending the API]
8. [Notes & Best Practices]

---

## What is a REST API?

A **REST API** (Representational State Transfer Application Programming Interface) is a way for programs to communicate over the web using HTTP methods. REST APIs treat data as resources, each with a unique URL, and use standard HTTP methods to perform actions:

- **GET**: Retrieve data
- **POST**: Create new data
- **PUT**: Update existing data
- **DELETE**: Remove data

REST APIs are stateless (each request is independent) and usually return data in JSON format.

---

## Project Structure

```
forum-api/
│── app.py
│── routes/
│     └── posts.py
│── models/
│     └── post.py
│── data/
│     └── db.py
│── requirements.txt 
|__ README.md
```

---

## Setup Instructions

### 1. Install Python
- Download and install Python 3.14 from [python.org](https://www.python.org/downloads/).
- Make sure `python` and `pip` are available in your terminal.

### 2. Install Flask
Open your terminal in the `forum-api` folder and run:

```bash
pip install flask
```

---

## Running the API

1. Open a terminal in the `forum-api` directory.
2. Start the server:
   ```bash
   python app.py
   ```
3. The API will be available at: [http://127.0.0.1:5000]

---

## API Endpoints & Usage

### 1. Home (Health Check)
- **GET /**
- Returns a simple message to confirm the API is running.

**Example:**
```
curl http://127.0.0.1:5000/
```

---

### 2. Get All Posts
- **GET /posts**
- Returns a list of all forum posts.

**Example:**
```
curl http://127.0.0.1:5000/posts
```

**Response:**
```json
[
  {"id": 1, "title": "First Post", "content": "Hello World"},
  ...
]
```

---

### 3. Get Single Post
- **GET /posts/<id>**
- Returns a single post by its ID.

**Example:**
```
curl http://127.0.0.1:5000/posts/2
```

**Response:**
```json
{"id": 2, "title": "Second Post", "content": "Learning Flask"}
```

---

### 4. Create a New Post
- **POST /posts**
- Adds a new post. Requires JSON body with `title` and `content`.

**Example:**
```
curl -X POST http://127.0.0.1:5000/posts -H "Content-Type: application/json" -d '{"title": "New Post", "content": "This is a new post."}'
```

**Response:**
```json
{"id": 11, "title": "New Post", "content": "This is a new post."}
```

---

### 5. Update a Post
- **PUT /posts/<id>**
- Updates an existing post. Requires JSON body with `title` and/or `content`.

**Example:**
```
curl -X PUT http://127.0.0.1:5000/posts/1 -H "Content-Type: application/json" -d '{"title": "Updated Title"}'
```

**Response:**
```json
{"id": 1, "title": "Updated Title", "content": "Hello World"}
```

---

### 6. Delete a Post
- **DELETE /posts/<id>**
- Deletes a post by its ID.

**Example:**
```
curl -X DELETE http://127.0.0.1:5000/posts/1
```

**Response:**
```json
{"message": "Post deleted successfully"}
```

---

## How the Code Works

- **Flask App Setup:**
  - `app = Flask(__name__)` creates the web server.
- **In-Memory Database:**
  - `posts` is a Python list acting as a fake database.
- **Routes:**
  - Each `@app.route` defines a URL and allowed HTTP methods.
  - Functions handle requests, process data, and return JSON responses.
- **CRUD Operations:**
  - **Create:** Adds a new post to the list.
  - **Read:** Returns all or a single post.
  - **Update:** Modifies a post if it exists.
  - **Delete:** Removes a post from the list.
- **Error Handling:**
  - Returns a 404 error if a post is not found.
- **Auto-Increment ID:**
  - New posts get an ID one higher than the current highest.

---

## Extending the API

- **Persistent Storage:**
  - Connect to a real database (e.g., SQLite, PostgreSQL) for permanent data.
- **Authentication:**
  - Add user login and permissions.
- **Validation:**
  - Check for missing fields or invalid data in requests.
- **Pagination:**
  - Limit the number of posts returned per request.
- **Deployment:**
  - Use a production server (e.g., Gunicorn) and deploy to cloud platforms.

---

## Notes & Best Practices

- This API is for learning/demo purposes. Data is lost when the server restarts.
- Always validate and sanitize user input in real-world apps.
- Use environment variables for configuration (e.g., debug mode, database URLs).
- Write tests for your endpoints.

---

## Summary

This project demonstrates a full REST API using Flask, covering all CRUD operations with clear code and comments. 

## To Push code to Github using git commands

git init 
git add .
git commit -am "initial Commit"
git branch -M main
git remote add origin (https://github.com/abdul-moiz007/forumm-apii)
git push origin main

## GitHub

https://github.com/abdul-moiz007/forumm-apii
