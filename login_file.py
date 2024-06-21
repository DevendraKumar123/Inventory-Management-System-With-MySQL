import tkinter as tk
from tkinter import messagebox
import pymysql
import subprocess


def validate_login(username, password):
    try:
        conn = pymysql.connect(
            host="localhost",  # Change this to your MySQL server host
            user="root",  # Change this to your MySQL username
            password="root",  # Change this to your MySQL password
            database="ims"
        )
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username=%s AND password=%s', (username, password))
        result = cursor.fetchone()
        conn.close()
        return result is not None
    except pymysql.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return False

def submit_login():
    username = entry_username.get()
    password = entry_password.get()
    
    # if validate_login(username, password):
    #     messagebox.showinfo("Login", "Login successful!")
    #     # Code to open a new page or perform another action
    # else:
    #     messagebox.showerror("Login", "Invalid username or password")
    
    if validate_login(username, password):
        messagebox.showinfo("Login", "Login successful!")
        root.destroy()
        subprocess.run(["python", "desh_board.py"])
    else:
        messagebox.showerror("Login", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Login Form")
root.geometry('600x600')

# Username label and entry
label_username = tk.Label(root, text="Username")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Password label and entry
label_password = tk.Label(root, text="Password")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Submit button
button_submit = tk.Button(root, text="Submit", command=submit_login)
button_submit.pack(pady=20)

root.mainloop()
