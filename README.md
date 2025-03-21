# GenAI Project using Hugging Face API

## Requirements

### Backend

- **FastAPI**: API Builder 
- **Uvicorn**: ASGI Server
- **Pydantic**: Data Validation/Settings Management
- **Transformers**: Language Processor
- **FastAPI CORS Middleware**: CORS Middleware

### Frontend

- **React**: Javascript Library for user interfaces
- **Axios**: HTTP client for browser

## Installation

Install the required packages using pip:

- Install FastAPI:
  ```sh
  pip install fastapi
  ```

- Install Uvicorn:
  ```sh
  pip install uvicorn
  ```

- Install Pydantic:
  ```sh
  pip install pydantic
  ```

- Install Transformers:
  ```sh
  pip install transformers
  ```

- Install FastAPI CORS Middleware:
  ```sh
  pip install fastapi[all]
  ```

## Commands

- Run/Restart Uvicorn:
  ```sh
  uvicorn backend:app --reload
  ```
  (start the backend.py file - if you rename "backend.py" file, you must update command to match name)

## Connection

Navigate to http://127.0.0.1:8000 in your browser for local connection to the Uvicorn instance.

## Frontend

To view the frontend, open the `index.html` file in your browser. You can do this by navigating to the file location in your file explorer and double-clicking on the `index.html` file, or by dragging and dropping the file into your browser window.