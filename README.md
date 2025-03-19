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

## Commands
Install the required packages using pip:

- Install Uvicorn:
  ```sh
  pip install uvicorn
  ```
(installs disposable server to use for hosting AI chat model)

- Run/Restart Uvicorn:
  ```sh
  uvicorn backend:app --reload
  ```
(start the backend.py file - if you rename "backend.py" file, you must update command to match name)

## Connection 

navigate to http://127.0.0.1:8000 in browser for local connection to uvicorn instance