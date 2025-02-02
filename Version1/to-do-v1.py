import tkinter as tk
from tkinter import messagebox

# Function to add a task
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to mark a task as done
def mark_done():
    try:
        selected_task_index = listbox.curselection()[0]
        task = listbox.get(selected_task_index)
        listbox.itemconfig(selected_task_index, {'bg': 'light gray', 'fg': 'gray'})
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as done.")

# Function to delete a task
def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Function to save tasks to a file
def save_tasks():
    with open("tasks.txt", "w") as file:
        tasks = listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")

# Function to load tasks from a file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

# Main application window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")

# Entry widget for adding tasks
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Buttons for adding, marking as done, and deleting tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

mark_done_button = tk.Button(root, text="Mark as Done", command=mark_done)
mark_done_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Listbox to display tasks
listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=10)

# Load tasks from file when the app starts
load_tasks()

# Save tasks to file when the app is closed
root.protocol("WM_DELETE_WINDOW", save_tasks)

# Run the application
root.mainloop()
