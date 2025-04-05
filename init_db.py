from app import db, Task

# Create the database and add sample tasks
with db.app_context():
    db.create_all()
    sample_task = Task(title="Sample Task", description="This is a sample task.")
    db.session.add(sample_task)
    db.session.commit()