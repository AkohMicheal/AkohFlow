from flask import Flask
app = Flask(__name__)
#This sets up a basic Flask application.
# This imports the Flask class from the flask module and creates an instance of it.
@app.route('/')
def home():
    return "Welcome to the Task Management App!"
@app.route('/tasks')
def tasks():
    return "Here are your tasks!"
#This defines the home route and a tasks route for the application.
if __name__ == '__main__':
    app.run(debug=True)
# This is a simple Flask application that serves as a starting point for a task management app.

from flask import Flask, render_template
# This imports the Flask class from the flask module and creates an instance of it.
app = Flask(__name__)
# This sets up a basic Flask application.
@app.route('/')
def home():
    return render_template('home.html')
# This defines the home route and a tasks route for the application.
@app.route('/tasks')
def tasks():
    return render_template('tasks.html')
# This defines the tasks route and renders a template for it.
# For now we will just render a simple HTML page.
if __name__ == '__main__':
    app.run(debug=True)
# This runs the application in debug mode, which is useful for development.

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# This imports the Flask class from the flask module and creates an instance of it.
app = Flask(__name__)
# This sets up a basic Flask application.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Configure the database URI and other settings for SQLAlchemy.
# This sets the database URI and disables track modifications to save memory.
db = SQLAlchemy(app)
# Initialize the database with the Flask app.
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.text(200), nullable=True)
    completed = db.Column(db.Boolean, default=False)
    # This defines the Task model with columns for id, title, description, and completed status.
    with app.app_context():
        db.create_all()
# Create the database tables if they don't exist.
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/tasks')
def tasks():
    all_tasks = Task.query.all()
    print(all_tasks)  # Debugging
    return render_template('tasks.html', tasks=all_tasks)
# This defines the tasks route and renders a template for it.
if __name__ == '__main__':
    app.run(debug=True)
# This runs the application in debug mode, which is useful for development.

from flask import Flask, request, redirect, url_for
# This imports the Flask class from the flask module and creates an instance of it.
@app.route('/add_task', methods=['POST'])
def add_task():
    title = request.form['title']
    description = request.form['description']
    new_task = Task(title=title, description=description)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('tasks'))
# This defines the add_task route to handle form submissions for adding new tasks.
@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task_to_delete = Task.query.get_or_404(task_id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for('tasks'))
# This defines the delete_task route to handle form submissions for deleting tasks.
@app.route('/update_task/<int:task_id>', methods=['POST'])
def update_task(task_id):
    task_to_update = Task.query.get_or_404(task_id)
    task_to_update.completed = not task_to_update.completed
    db.session.commit()
    return redirect(url_for('tasks'))
# This defines the update_task route to handle form submissions for updating tasks.