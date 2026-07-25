import tkinter as tk
import secrets
import string

def generate_password():
    try:
        password_length = int(entry.get())
        if password_length < 10 or password_length > 20:
            output_label.config(text="Length must be between 10 and 20 characters", fg="red")
            return
        safe_symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?/~`"
        characters = string.ascii_letters + string.digits + safe_symbols
        password = "".join(secrets.choice(characters) for _ in range(password_length))

        entry.delete(0, tk.END)
        entry.insert(0, password)
        output_label.config(text="Password generated successfully!", fg="green")
    except ValueError:
        output_label.config(text="Please enter a valid number", fg="red")

   
root = tk.Tk()
root.title("Password generator")
root.geometry("500x500")
root.config(bg="navy")

label = tk.Label(root, text= "enter password length", font=("Arial", 14), fg="white", bg="navy")
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), justify="right")
entry.insert(0, "8")
entry.pack(pady=10)

output_label = tk.Label(root, text="", font=("Arial", 14), fg="white", bg="navy")
output_label.pack(pady=20)

button = tk.Button(root, text="Generate Password", font=("Arial", 14), fg="white", bg="green" , command=generate_password)
button.pack(pady=10)

root.mainloop()