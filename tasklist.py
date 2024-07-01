import tkinter as tk
from tkinter import messagebox

class TaskListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task List Application")

        self.tasks = []

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, width=50, height=10, selectbackground="#a6a6a6")
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.clear_button = tk.Button(self.root, text="Clear All Tasks", command=self.clear_tasks)
        self.clear_button.pack(pady=5)

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def clear_tasks(self):
        self.tasks = []
        self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks):
            display_text = f"{index + 1}. {task}"
            self.task_listbox.insert(tk.END, display_text)
            # Apply alternating colors
            if index % 2 == 0:
                self.task_listbox.itemconfig(index, {'bg': '#f0f0f0'})
            else:
                self.task_listbox.itemconfig(index, {'bg': '#d9d9d9'})

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskListApp(root)
    root.mainloop()
