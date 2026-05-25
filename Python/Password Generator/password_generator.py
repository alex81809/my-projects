import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password length should be at least 4.")
            return
        
        # Define characters to use
        characters = string.ascii_letters + string.digits + string.punctuation
        # Generate random password
        password = "".join(random.choice(characters) for i in range(length))
        
        # Display password in the entry box
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length.")

def copy_to_clipboard():
    password = entry_password.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Success", "Password copied to clipboard!")

# --- UI Setup ---
root = tk.Tk()
root.title("PassGen - Password Generator")
root.geometry("400x250")
root.padx = 20

# Length Label and Entry
label_inst = tk.Label(root, text="Enter Password Length:", font=("Arial", 10))
label_inst.pack(pady=10)

entry_length = tk.Entry(root, font=("Arial", 12), width=10, justify='center')
entry_length.insert(0, "12")  # Default length
entry_length.pack()

# Generate Button
btn_generate = tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
btn_generate.pack(pady=15)

# Password Display
entry_password = tk.Entry(root, font=("Courier", 12), width=30, justify='center')
entry_password.pack(pady=5)

# Copy Button
btn_copy = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
btn_copy.pack(pady=5)

root.mainloop()
