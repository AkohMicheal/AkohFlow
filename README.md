# Task Management App

A Flask-based web application for managing tasks. This app allows users to register, log in, and manage their tasks with features like adding, editing, deleting, searching, and filtering tasks.

---

## Features

- **User Authentication**: Register, log in, and log out securely.
- **Task Management**: Add, edit, delete, and mark tasks as complete or incomplete.
- **Search and Filter**: Search tasks by title or description and filter by completion status.
- **Pagination**: View tasks in a paginated format.
- **Responsive Design**: User-friendly interface with Bootstrap styling.

---

## Installation

### Prerequisites

- Python 3.8 or higher
- PostgreSQL installed and running

### Steps

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd task_management_app
   ```

---

## Project Structure

```plaintext
task_management_app/
├── app.py               # Main application file
├── init_db.py           # Script to initialize the database
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables
├── templates/           # HTML templates
│   ├── layout.html
│   ├── index.html
│   ├── tasks.html
│   ├── login.html
```
