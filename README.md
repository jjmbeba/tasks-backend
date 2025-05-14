# Tasks App Backend

This is the backend for a simple note/task management application, built with **FastAPI**. It provides a RESTful API for managing tasks, including creating, reading, updating, and deleting tasks. The backend is designed to work seamlessly with a React + Vite frontend (see the `frontend` directory).

## Features
- FastAPI-based REST API
- In-memory task storage (no database required)
- CORS enabled for local frontend development
- Simple data models using Pydantic

## Requirements
- Python 3.8+
- (Recommended) Virtual environment tool (e.g., `venv`, `virtualenv`)

## Installation
1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd backend
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Server
Start the FastAPI server using Uvicorn:
```bash
uvicorn main:app --reload
```
- The API will be available at `http://localhost:8000` by default.
- Interactive API docs: `http://localhost:8000/docs`

## API Endpoints

### `GET /`
- Returns a simple greeting message.

### `GET /tasks`
- Returns a list of all tasks.

### `POST /tasks`
- Creates a new task.
- **Request body:**
  ```json
  {
    "name": "Task name",
    "description": "Task description"
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "name": "Task name",
    "description": "Task description",
    "is_completed": false
  }
  ```

### `PUT /tasks/{task_id}`
- Updates an existing task.
- **Request body:** (any subset of fields)
  ```json
  {
    "name": "Updated name",
    "description": "Updated description",
    "is_completed": true
  }
  ```

### `DELETE /tasks/{task_id}`
- Deletes a task by ID.

## Data Models
- **Task**: `{ id: int, name: str, description: str, is_completed: bool }`
- **TaskCreate**: `{ name: str, description: str }`
- **TaskUpdate**: `{ name?: str, description?: str, is_completed?: bool }`

## CORS & Frontend
- CORS is enabled for `http://localhost:3000` and `http://localhost:5173` to support local frontend development.

## Notes
- This backend uses in-memory storage; all data will be lost when the server restarts.
- For production, consider adding persistent storage (e.g., a database).

## License
MIT 
