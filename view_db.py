from app import db, Task, app  # Import the app object

with app.app_context():
    tasks = Task.query.all()
    for task in tasks:
        print(f"ID: {task.id}, Title: {task.title}, Description: {task.description}, Completed: {task.completed}")