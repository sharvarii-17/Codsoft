import tkinter as tk
from tkinter import ttk, messagebox
from task import Task

class ToDoApp:                          
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []                 #empty set of lists initialized

        self.create_widgets()

    def create_widgets(self):
        # Style: Treeview widget headings for bold
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Arial', 12, 'bold'))

        # Entry Frame for widgets
        entry_frame = ttk.Frame(self.root)
        entry_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        ttk.Label(entry_frame, text="Enter a task:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.task_entry = ttk.Entry(entry_frame, width=30)
        self.task_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(entry_frame, text="Due Date:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.due_date_entry = ttk.Entry(entry_frame, width=15)
        self.due_date_entry.grid(row=0, column=3, padx=5, pady=5)

        ttk.Button(entry_frame, text="Add Task", command=self.add_task).grid(row=0, column=4, padx=5, pady=5)

        # Treeview to display tasks in a table format with headings
        self.tasks_tree = ttk.Treeview(self.root, columns=("Title", "Due Date", "Status"), show="headings", selectmode="browse", height=10)
        self.tasks_tree.heading("Title", text="Title")
        self.tasks_tree.heading("Due Date", text="Due Date")
        self.tasks_tree.heading("Status", text="Status")
        self.tasks_tree.column("Title", width=200)
        self.tasks_tree.column("Due Date", width=100)
        self.tasks_tree.column("Status", width=100)
        self.tasks_tree.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        #delete selected lists
        ttk.Button(self.root, text="Delete Task", command=self.delete_selected_task).grid(row=2, column=0, padx=10, pady=10, sticky="w")

    def add_task(self):
        title = self.task_entry.get()
        due_date = self.due_date_entry.get()

        if title:
            task = Task(title, due_date)
            self.tasks.append(task)
            self.update_tasks_tree()
            self.clear_entries()
        else:
            messagebox.showwarning("Empty Task", "Task title cannot be empty.")

    def update_tasks_tree(self):                                        # method to update tasks
        self.tasks_tree.delete(*self.tasks_tree.get_children())
        for task in self.tasks:
            status = "Completed" if task.completed else "Not Completed"
            self.tasks_tree.insert("", "end", values=(task.title, task.due_date, status))

    def delete_selected_task(self):                                     # method to delete tasks
        selected_item = self.tasks_tree.selection()

        if selected_item:
            index = int(selected_item[0][1:]) - 1
            del self.tasks[index]
            self.update_tasks_tree()

    def clear_entries(self):                                            # method to clear entries and due date
        self.task_entry.delete(0, tk.END)
        self.due_date_entry.delete(0, tk.END)
