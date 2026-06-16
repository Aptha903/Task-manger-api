from fastapi import FastAPI
from database.db import Base, engine
from routers import tasks
import models  # important so SQLAlchemy loads tables

# Create all tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager REST API",
    description="A REST API built with FastAPI and SQLite for managing tasks with CRUD operations.",
    version="1.0.0"
)

# Register routers
app.include_router(tasks.router)

@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Task Manager API is running!",
        "docs": "/docs"
    }
