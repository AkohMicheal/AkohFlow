# Task Management App

## Setup
1. Install dependencies:
   ```bash
   pip install flask flask-sqlalchemy
2. Run the application:
   python app.py
3. Access the app at
   Your current setup looks good for a basic task management app. However, here are a few optional improvements and additions you might consider to enhance functionality and structure:

---

### 1. **Add `index.html`**
If you haven't already created `index.html`, you need to add it to the templates folder to render the homepage. Here's an example:

```html
{% extends "layout.html" %}

{% block content %}
    <h1>Welcome to the Task Management App</h1>
    <p>Use the navigation bar to view or manage tasks.</p>
{% endblock %}
```

---

### 2. **Improve Error Handling**
Add error handling for cases where a task is not found or invalid data is submitted. For example:

```python
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404
```

You can create a `404.html` file in the templates folder to display a custom error page.

---

### 3. **Add Static Files**
You already have a `styles.css` file in the static folder. If you want to include additional assets like JavaScript or images, you can add them to the static folder. For example:

```
task_management_app/
├── static/
│   ├── styles.css
│   ├── script.js
│   ├── images/
│       ├── logo.png
```

---

### 4. **Enhance `tasks.html`**
You can add more functionality to `tasks.html`, such as:
- Buttons to delete or update tasks.
- A form to edit task details.

Example:
```html
<!-- Add delete and update buttons -->
<li>
    <strong>{{ task.title }}</strong><br>
    {{ task.description }}<br>
    {% if task.completed %}
        <span>Status: Completed</span>
    {% else %}
        <span>Status: Incomplete</span>
    {% endif %}
    <form action="{{ url_for('delete_task', task_id=task.id) }}" method="POST" style="display:inline;">
        <button type="submit">Delete</button>
    </form>
    <form action="{{ url_for('update_task', task_id=task.id) }}" method="POST" style="display:inline;">
        <button type="submit">Toggle Status</button>
    </form>
</li>
```

---

### 5. **Database Initialization Script**
If you want to initialize the database with some default tasks, you can create a script to populate the database. For example:

```python
from app import db, Task

# Create the database and add sample tasks
with db.app_context():
    db.create_all()
    sample_task = Task(title="Sample Task", description="This is a sample task.")
    db.session.add(sample_task)
    db.session.commit()
```

Run this script once to initialize the database:
```bash
python init_db.py
```

---

### 6. **Add JavaScript (Optional)**
If you want to add interactivity (e.g., confirmation dialogs for deleting tasks), you can include a `script.js` file in the static folder and reference it in `layout.html`:
```html
<script src="{{ url_for('static', filename='script.js') }}"></script>
```

Example `script.js`:
```javascript
document.querySelectorAll('form[action*="delete_task"]').forEach(form => {
    form.addEventListener('submit', function (e) {
        if (!confirm('Are you sure you want to delete this task?')) {
            e.preventDefault();
        }
    });
});
```

---

### 7. **Test Your Application**
Run your Flask app and test all routes (`/`, `/tasks`, `/add_task`, `/delete_task`, `/update_task`) to ensure everything works as expected:
```bash
python app.py
```

---

### 8. **Optional: Add a README File**
Add a `README.md` file to document how to set up and run your application. Example:
```markdown
# Task Management App

## Setup
1. Install dependencies:
   ```bash
   pip install flask flask-sqlalchemy
   ```
2. Run the application:
   ```bash
   python app.py
   ```
3. Access the app at `http://127.0.0.1:5000`.

## Features
- Add, update, and delete tasks.
- View all tasks.
```

---

### Summary
- **Required**: Add `index.html` if not already created.
- **Optional**: Add error handling, JavaScript, database initialization, and a README file.
- Test your application thoroughly to ensure all features work as expected.

Let me know if you need help with any of these steps at akohmicheal@gmail.com!