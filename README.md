# Task Manager REST API

A RESTful API built with **FastAPI**, **MySQL**, and **SQLAlchemy** for managing tasks with full CRUD operations.

## Tech Stack
- Python, FastAPI, SQLAlchemy, MySQL, Pydantic, Postman

## Features
- Create, Read, Update, Delete tasks
- Filter tasks by status (pending / in_progress / completed)
- Auto-generated interactive API docs via Swagger UI
- MVC architecture with clean separation of concerns

## Project Structure
```
task_manager_api/
├── main.py               # FastAPI app entry point
├── requirements.txt
├── .env.example
├── database/
│   └── db.py             # DB connection & session
├── models/
│   └── task.py           # SQLAlchemy Task model
├── schemas/
│   └── task_schema.py    # Pydantic request/response schemas
└── routers/
    └── tasks.py          # All CRUD route handlers
```

## Setup

### 1. Clone & install dependencies
```bash
git clone https://github.com/Aptha903/task-manager-api
cd task_manager_api
pip install -r requirements.txt
```

### 2. Setup MySQL database
```sql
CREATE DATABASE task_manager_db;
```

### 3. Configure environment
```bash
cp .env.example .env
# Edit .env with your MySQL credentials
```

### 4. Run the server
```bash
uvicorn main:app --reload
```

### 5. Open Swagger UI
Visit: http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/tasks/` | Create a new task |
| GET | `/tasks/` | Get all tasks (optional: `?status_filter=pending`) |
| GET | `/tasks/{id}` | Get task by ID |
| PUT | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |

## Example Request (POST /tasks/)
```json
{
  "title": "Complete project report",
  "description": "Write and submit final ML project report",
  "status": "pending",
  "due_date": "2026-06-20"
}
```

## Example Response
```json
{
  "id": 1,
  "title": "Complete project report",
  "description": "Write and submit final ML project report",
  "status": "pending",
  "due_date": "2026-06-20",
  "created_at": "2026-06-16T10:00:00",
  "updated_at": null
}
```
