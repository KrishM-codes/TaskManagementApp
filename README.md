
# Task Manager API

This is a Django-based API for managing tasks and user authentication. It provides features for creating users, logging in, and managing tasks.

## Table of Contents

- [Project Setup](#project-setup)
- [API Endpoints](#api-endpoints)
  - [User Registration](#user-registration)
  - [Token Authentication](#token-authentication)
  - [Task Management](#task-management)
- [Testing the API](#testing-the-api)
  - [Testing User Registration](#testing-user-registration)
  - [Testing Token Authentication](#testing-token-authentication)
  - [Testing Task Management](#testing-task-management)
- [Testing with Curl Commands](#testing-with-curl-commands)

## Project Setup

To run this project locally, follow the steps below:

### 1. Clone the repository:

```bash
git clone https://github.com/KrishM-codes/TaskManagementApp/
cd task-manager
```

### 2. Install dependencies:

Make sure you have Python 3.x installed. Then, create a virtual environment and install dependencies.

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
pip install -r requirements.txt
```

### 3. Apply migrations:

```bash
python manage.py migrate
```

### 4. Create a superuser (optional, for Django admin access):

```bash
python manage.py createsuperuser
```

### 5. Run the development server:

```bash
python manage.py runserver
```

The API will be running at `http://127.0.0.1:8000/`.

---

## API Endpoints

Here are the available API endpoints:

### User Registration

- **URL:** `/register/`
- **Method:** `POST`
- **Request Body:**

```json
{
  "username": "your_username",
  "email": "your_email@example.com",
  "password": "your_password"
}
```

- **Response:**

```json
{
  "id": 1,
  "username": "your_username",
  "email": "your_email@example.com"
}
```

---

### Token Authentication

1. **Obtain Token**
   - **URL:** `/api/token/`
   - **Method:** `POST`
   - **Request Body:**

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

   - **Response:**

```json
{
  "access": "your_access_token",
  "refresh": "your_refresh_token"
}
```

2. **Refresh Token**
   - **URL:** `/api/token/refresh/`
   - **Method:** `POST`
   - **Request Body:**

```json
{
  "refresh": "your_refresh_token"
}
```

   - **Response:**

```json
{
  "access": "your_new_access_token"
}
```

3. **Verify Token**
   - **URL:** `/api/token/verify/`
   - **Method:** `POST`
   - **Request Body:**

```json
{
  "token": "your_access_token"
}
```

   - **Response:**

```json
{
  "detail": "Token is valid"
}
```

---

### Task Management

- **URL:** `/api/tasks/`
- **Method:** `GET` (List all tasks)

```bash
curl -X GET http://127.0.0.1:8000/api/tasks/ -H "Authorization: Bearer <your_access_token>"
```

- **Response:**

```json
[
  {
    "id": 1,
    "title": "Sample Task",
    "description": "Task description",
    "completed": false,
    "created_at": "2024-11-12T12:00:00Z",
    "updated_at": "2024-11-12T12:00:00Z"
  }
]
```

- **URL:** `/api/tasks/`
- **Method:** `POST` (Create a new task)
- **Request Body:**

```json
{
  "title": "New Task",
  "description": "Task description"
}
```

- **Response:**

```json
{
  "id": 2,
  "title": "New Task",
  "description": "Task description",
  "completed": false,
  "created_at": "2024-11-12T12:30:00Z",
  "updated_at": "2024-11-12T12:30:00Z"
}
```

- **URL:** `/api/tasks/{id}/`
- **Method:** `PUT` (Update an existing task)
- **Request Body:**

```json
{
  "title": "Updated Task",
  "description": "Updated task description",
  "completed": true
}
```

- **Response:**

```json
{
  "id": 2,
  "title": "Updated Task",
  "description": "Updated task description",
  "completed": true,
  "created_at": "2024-11-12T12:30:00Z",
  "updated_at": "2024-11-12T12:45:00Z"
}
```

- **URL:** `/api/tasks/{id}/`
- **Method:** `DELETE` (Delete a task)
- **Response:**

```json
{
  "detail": "Deleted successfully"
}
```

---

## Testing the API

### Testing User Registration

Use the following `curl` command to register a new user:

```bash
curl -X POST http://127.0.0.1:8000/register/ -d '{"username": "new_user", "email": "user@example.com", "password": "password123"}' -H "Content-Type: application/json"
```

### Testing Token Authentication

#### Obtain Token

```bash
curl -X POST http://127.0.0.1:8000/api/token/ -d '{"username": "new_user", "password": "password123"}' -H "Content-Type: application/json"
```

#### Refresh Token

```bash
curl -X POST http://127.0.0.1:8000/api/token/refresh/ -d '{"refresh": "your_refresh_token"}' -H "Content-Type: application/json"
```

#### Verify Token

```bash
curl -X POST http://127.0.0.1:8000/api/token/verify/ -d '{"token": "your_access_token"}' -H "Content-Type: application/json"
```

### Testing Task Management

#### List Tasks

```bash
curl -X GET http://127.0.0.1:8000/api/tasks/ -H "Authorization: Bearer <your_access_token>"
```

#### Create Task

```bash
curl -X POST http://127.0.0.1:8000/api/tasks/ -d '{"title": "New Task", "description": "Task description"}' -H "Authorization: Bearer <your_access_token>" -H "Content-Type: application/json"
```

#### Update Task

```bash
curl -X PUT http://127.0.0.1:8000/api/tasks/1/ -d '{"title": "Updated Task", "description": "Updated task description", "completed": true}' -H "Authorization: Bearer <your_access_token>" -H "Content-Type: application/json"
```

#### Delete Task

```bash
curl -X DELETE http://127.0.0.1:8000/api/tasks/1/ -H "Authorization: Bearer <your_access_token>"
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
