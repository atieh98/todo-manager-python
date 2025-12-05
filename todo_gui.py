import tkinter as tk
from tkinter import messagebox
import time
from datetime import datetime
import pytz
from todo_manager import TodoManager

tm = TodoManager()

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("TODO Manager")
        self.root.geometry("520x520")
        self.root.configure(bg="#f2f2f2")

        # Title Bar
        title = tk.Label(
            root, text="📝 TODO MANAGER",
            font=("Arial", 18, "bold"),
            bg="#4a90e2", fg="white", pady=10
        )
        title.pack(fill="x")

        # Main Listbox
        frame_list = tk.Frame(root, bg="#f2f2f2")
        frame_list.pack(pady=10)

        self.listbox = tk.Listbox(
            frame_list, width=58, height=15,
            bg="white", fg="#333333",
            selectbackground="#add8e6",
            font=("Arial", 10)
        )
        self.listbox.pack()

        # Buttons Panel
        frame_btn = tk.Frame(root, bg="#f2f2f2")
        frame_btn.pack(pady=15)

        btn = {
            "width": 10, "height": 1,
            "fg": "white", "font": ("Arial", 10, "bold"),
            "bd": 0
        }

        tk.Button(frame_btn, text="Refresh", bg="#4a90e2", command=self.refresh, **btn).grid(row=0, column=0, padx=5)
        tk.Button(frame_btn, text="Add", bg="#5cb85c", command=self.add, **btn).grid(row=0, column=1, padx=5)
        tk.Button(frame_btn, text="Done", bg="#f0ad4e", command=self.done, **btn).grid(row=0, column=2, padx=5)
        tk.Button(frame_btn, text="Delete", bg="#d9534f", command=self.delete, **btn).grid(row=0, column=3, padx=5)

        self.refresh()

    # --------------------------------
    # Refresh List
    def refresh(self):
        self.listbox.delete(0, tk.END)

        for i, t in enumerate(tm.tasks):

            text = f"{i+1}. {t.title} | {t.category} | P{t.priority}"

            if t.completed:
                text += " | [DONE]"
            else:
                if t.deadline:
                    left = int(t.deadline - time.time())
                    if left > 0:
                        text += f" | {left//60}m {left%60}s left"
                    else:
                        text += " | expired"

            self.listbox.insert(tk.END, text)

            if t.completed:
                self.listbox.itemconfig(tk.END, fg="#888888")

    # --------------------------------
    # Add New Task
    def add(self):
        win = tk.Toplevel()
        win.title("Add Task")
        win.geometry("360x420")
        win.configure(bg="#fafafa")

        tk.Label(win, text="Add New Task", font=("Arial", 14, "bold"), bg="#fafafa").pack(pady=10)

        def field(lbl):
            tk.Label(win, text=lbl, font=("Arial", 10, "bold"), bg="#fafafa").pack()
            e = tk.Entry(win, width=30)
            e.pack(pady=4)
            return e

        e1 = field("Title")
        e2 = field("Category")

        # Priority Input
        tk.Label(win, text="Priority (1-3):", font=("Arial", 10, "bold"), bg="#fafafa").pack()
        priority_entry = tk.Entry(win, width=30)
        priority_entry.pack(pady=4)

        tk.Label(
            win,
            text="(Hint: 1 = Low | 2 = Medium | 3 = High)",
            font=("Arial", 9),
            bg="#fafafa",
            fg="#555"
        ).pack(pady=2)

        # Deadline
        tk.Label(win, text="Deadline (YYYY-MM-DD HH:MM):", font=("Arial", 10, "bold"), bg="#fafafa").pack()
        deadline_entry = tk.Entry(win, width=30)
        deadline_entry.pack(pady=4)

        def save():
            title = e1.get().strip()
            category = e2.get().strip() or "General"

            # Priority Validation
            try:
                priority = int(priority_entry.get())
                if priority not in [1, 2, 3]:
                    raise ValueError
            except:
                messagebox.showerror("Error", "Priority must be 1, 2, or 3.")
                return

            # Deadline (KST)
            try:
                dt = datetime.strptime(deadline_entry.get(), "%Y-%m-%d %H:%M")
                kst = pytz.timezone("Asia/Seoul")
                dt = kst.localize(dt)
                deadline = dt.timestamp()
            except:
                messagebox.showerror("Error", "Invalid date format!")
                return

            tm.add_task(title, category, priority, deadline)
            self.refresh()
            win.destroy()

        tk.Button(
            win, text="Save",
            command=save,
            bg="#5cb85c", fg="white",
            font=("Arial", 10, "bold"),
            width=12, bd=0
        ).pack(pady=15)

    # --------------------------------
    # Mark Task Done
    def done(self):
        sel = self.listbox.curselection()
        if sel:
            tm.mark_done(sel[0])
            self.refresh()

    # --------------------------------
    # Delete Task
    def delete(self):
        sel = self.listbox.curselection()
        if sel:
            tm.delete_task(sel[0])
            self.refresh()


root = tk.Tk()
App(root)
root.mainloop()
