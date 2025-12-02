# 📝 To Do List – Python CRUD

A simple and organized application to manage tasks using **CRUD operations (Create, Read, Update, Delete)**. This project was built with **Python** and is suitable for both learning and personal use.

---

## 📌 Overview

This project provides a task management system where each item contains:

* **Title**
* **Description**
* **Status** (pending, in progress, completed)
* **Creation and completion dates**

Perfect for:

* Learning CRUD concepts in Python
* Study projects
* Personal organization
* Serving as a base for bigger applications

---

## 🧱 Technologies Used

* **Python**: version used in development
* **Framework/Library**: Flask / Django / FastAPI / Tkinter / CLI
* **Database**: SQLite / PostgreSQL / JSON / Other
* **Additional dependencies**: list them here

---

## 📂 Project Structure

```
project/
│── app/                 # Core CRUD logic
│── models/              # Data models (e.g., Task)
│── routes/ or views/    # Routes or UI
│── tests/               # Tests
│── README.md            # Documentation
```

*(Adjust according to your real structure.)*

---

## ✅ Features

* ➕ Create tasks with title and description
* 📄 List all tasks
* ✏️ Update title, description, and status
* ✔️ Mark tasks as completed
* ❌ Delete tasks
* 🔍 (Optional) Search or filter by text/status

---

## 📊 Data Model

Each task contains:

* **id** – unique identifier
* **title** – short description of the task
* **description** – additional details
* **status** – pending / in_progress / completed
* **created_at** – generated automatically
* **completed_at** – set when the task is completed

If you have other models (User, Category, etc.), describe them here.

---

## 🔁 CRUD Operations

### **Create** – Add a new task

Only the title is required; description is optional.

### **Read** – List tasks

Displays all tasks or applies filters if implemented.

### **Update** – Modify a task

Allows updating any field, including status.

### **Delete** – Remove a task

Deletes permanently or with confirmation (if implemented).

### (Optional) REST Endpoints

```
GET    /tasks          → list tasks
POST   /tasks          → create task
PUT    /tasks/{id}     → update task
DELETE /tasks/{id}     → delete task
```

---

## ▶️ How to Run

1. **Clone the repository**
2. **Install dependencies** listed in the requirements file
3. Run the main file, for example:

   ```bash
   python main.py
   ```
4. Interact through the terminal or browser (depending on implementation)

---

## 👤 User Flow

1. User opens the application
2. Views existing tasks
3. Creates new tasks
4. Updates task progress
5. Deletes unnecessary or completed tasks

---

## 📌 Business Rules

* Title is required
* Default status: **pending**
* Creation date auto-generated
* Fields validated according to requirements

---

## 🧪 Tests

You may include:

* Manual test scenarios
* Automated tests (unittest or pytest)
* Cases like: empty task creation, update nonexistent task, delete nonexistent task

---

## 🚧 Limitations and Future Improvements

**Current limitations:**

* No user authentication
* Limited filters
* Basic interface

**Possible improvements:**

* Login and multi-user support
* Filters by status, date, or keyword
* Notifications or reminders
* Full web interface or mobile app
