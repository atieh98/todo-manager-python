# TODO Manager (Python GUI Application)

## Overview

This project is a **GUI-based Task Management Application** developed in Python using `Tkinter`.  
It allows users to add, view, complete, delete, and track tasks with deadlines and priority levels.  
Each task can trigger an automatic alert when the deadline is reached.  
The program stores all tasks locally using Python’s `pickle` module.

This project was developed for the **Open Source Programming** course.

---

## Key Features

### Add New Tasks

Users can create tasks with:

- Title
- Category
- Priority (1 = low, 2 = medium, 3 = high)
- Deadline (KST — YYYY-MM-DD HH:MM)

**Screenshot:**  
![Add Task Window](Add_Task_Window.png)

---

### View Tasks (Main GUI)

Tasks are displayed with:

- Title
- Category
- Priority
- Remaining Time
- Expired status

**Screenshot:**  
![Main Window](Main_Window.png)

---

### ✔ Mark Tasks as Completed

Selecting a task and clicking **Done** marks it as completed.

**Screenshot:**  
![Selecting Task for Done](Selecting_a_Task_for_Done.png)

---

### ✔ Delete Tasks

Users can delete any selected task using the Delete button.

**Screenshot:**  
![Selecting Task for Delete](Selecting_a_Task_for_Delete.png)

---

### ✔ Automatic Deadline Alerts (Thread-Based)

A background thread waits until each task deadline.  
When the time is up, the console prints:

```
[ALERT] Deadline reached for: <task title>
```

**Screenshot:**  
![Deadline Alert in Terminal](Deadline_Alert_in_Terminal.png)

---

## 🧩 Project Structure

```
todo_project/
├── todo_gui.py
├── todo_manager.py
├── task.py
├── tasks.dat          # auto-created, not uploaded to GitHub
└── README.md
```

**Screenshot:**  
![Project Folder Structure](Project_Folder_Structure.png)

---

## 🛠 Requirements

Python **3.8+**

Modules used:

- tkinter
- time
- datetime
- threading
- pickle
- pytz

---

## ▶️ How to Run (VSCode / Terminal)

### 1. Open the project folder

```
cd "D:\open source software\todo_project"
```

### 2. Run the program

```
python todo_gui.py
```

**Screenshot:**  
![First Launch](First_Launch.png)

---

## 📝 How to Use the Application

### 1. Create a New Task

Click **Add**, fill the fields, and press Save.

**Screenshots:**  
![Creating a New Task](Creating_a_New_Task.png)  
![Creating a New Task 2](Creating_a_New_Task2.png)

---

### 2. Mark a Task as Done

Select the task → click **Done**.

**Screenshot:**  
![Marked as Done](Marked_as_Done.png)

---

### 3. Delete a Task

Select → click **Delete**.

**Screenshot:**  
![Deleted Task](Deleted_Task.png)

---

### 4. Deadline Alert Test

If deadline is reached, console prints an alert.

**Screenshot:**  
![Deadline Alert](Deadline_Alert.png)

---

## 📦 Data Persistence

All tasks are saved in `tasks.dat` using **pickle**.  
When reopening the program, saved tasks are loaded automatically.

**Screenshot:**  
![Persistence After Restart](Persistence_After_Restart.png)

---

## 🧪 Manual Testing Checklist

| Test             | Expected               |
| ---------------- | ---------------------- |
| Add Task         | Task appears in list   |
| Invalid Deadline | Error popup            |
| Mark Done        | Task marked completed  |
| Delete Task      | Removed from list      |
| Restart Program  | Tasks still exist      |
| Deadline Reached | Terminal alert printed |

(Use the screenshots above for documentation.)

---

## 📤 Submission Requirements

### ✔ Include:

- todo_gui.py
- todo_manager.py
- task.py
- README.md

### ❌ Do NOT include:

- tasks.dat
- \_\_pycache\_\_/

Add this to `.gitignore`:

```
tasks.dat
__pycache__/
*.pyc
```

---

## 🔍 Optional Future Improvements

- Edit tasks
- Sort tasks (by date/priority/category)
- Add search bar in GUI
- Use JSON or SQLite instead of pickle
- Add system notifications

---

## 🏁 Conclusion

This project demonstrates:

- GUI design with Tkinter
- Multithreading for alerts
- Local file persistence
- A clean, functional interface
- Manual testing and documentation

The application is simple but fully functional, and ideal for an academic open-source course.
