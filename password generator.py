import tkinter as tk
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def generate_and_display_password():
    length = int(length_entry.get())
    password = generate_password(length)
    generated_password_var.set(password)

def accept_password():
    username = username_entry.get()
    password = generated_password_var.get()
    if username and password:
        result_label.config(text=f"Username: {username}\nPassword: {password}")
    else:
        result_label.config(text="Please generate a password and enter a username.")

def reset_fields():
    username_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    generated_password_var.set("")
    result_label.config(text="")

# Create GUI window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
username_label = tk.Label(root, text="Enter username:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

length_label = tk.Label(root, text="Enter password length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password, bg="blue", fg="white", font=("Arial", 14))
generate_button.pack(pady=10)

generated_password_var = tk.StringVar()
generated_password_label = tk.Label(root, textvariable=generated_password_var, font=("Arial", 14))
generated_password_label.pack()

accept_button = tk.Button(root, text="Accept", command=accept_password, bg="green", fg="white", font=("Arial", 14))
accept_button.pack(pady=5)

reset_button = tk.Button(root, text="Reset", command=reset_fields, bg="red", fg="white", font=("Arial", 14))
reset_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()

# Start GUI event loop
root.mainloop()
