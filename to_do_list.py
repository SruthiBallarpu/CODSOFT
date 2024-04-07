import os
import json
import tkinter as tk
from tkinter import messagebox

# Function to load tasks from a JSON file
def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
        return tasks
    else:
        return []

# Function to save tasks to a JSON file
def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

# Function to refresh the task list
def refresh_task_list(task_list, tasks):
    task_list.delete(0, tk.END)
    for task in tasks:
        task_list.insert(tk.END, f"{task['title']} - {'Done' if task['done'] else 'Pending'}")

# Function to add a new task
def add_task(entry_task, task_list, tasks):
    title = entry_task.get()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    refresh_task_list(task_list, tasks)
    entry_task.delete(0, tk.END)

# Function to mark a task as done
def mark_task_done(task_list, tasks):
    try:
        selected_index = task_list.curselection()[0]
        tasks[selected_index]["done"] = True
        save_tasks(tasks)
        refresh_task_list(task_list, tasks)
    except IndexError:
        messagebox.showerror("Error", "Please select a task to mark as done!")

# Function to delete a task
def delete_task(task_list, tasks):
    try:
        selected_index = task_list.curselection()[0]
        del tasks[selected_index]
        save_tasks(tasks)
        refresh_task_list(task_list, tasks)
    except IndexError:
        messagebox.showerror("Error", "Please select a task to delete!")

# Main function
def main():
    tasks = load_tasks()

    root = tk.Tk()
    root.title("To-Do List")

    # Panel Frame
    panel_frame = tk.Frame(root, bg="#FFFFFF")  # Setting panel color
    panel_frame.grid(row=0, column=0, padx=10, pady=10)

    # Task Entry
    entry_task = tk.Entry(panel_frame, width=50)
    entry_task.grid(row=0, column=0, padx=5, pady=5)

    # Add Task Button
    button_add = tk.Button(panel_frame, text="Add Task", command=lambda: add_task(entry_task, task_list, tasks), bg="#4CAF50", fg="white")  # Setting button color
    button_add.grid(row=0, column=1, padx=5, pady=5)

    # Task List
    task_list = tk.Listbox(panel_frame, width=50)
    task_list.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
    refresh_task_list(task_list, tasks)

    # Mark as Done Button
    button_done = tk.Button(panel_frame, text="Mark as Done", command=lambda: mark_task_done(task_list, tasks), bg="#008CBA", fg="white")  # Setting button color
    button_done.grid(row=2, column=0, padx=5, pady=5)

    # Delete Task Button
    button_delete = tk.Button(panel_frame, text="Delete Task", command=lambda: delete_task(task_list, tasks), bg="#f44336", fg="white")  # Setting button color
    button_delete.grid(row=2, column=1, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
