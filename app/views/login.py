import tkinter as tk
from tkinter import messagebox
from app.services.auth import AuthService
from app.utils.style import apply_default

class LoginWindow(tk.Toplevel):
    def __init__(self, master, on_success):
        super().__init__(master)
        self.title("Login")
        self.geometry("320x200")
        self.on_success = on_success

        tk.Label(self, text="Username").grid(row=0, column=0, padx=8, pady=8)
        self.username = tk.Entry(self)
        self.username.grid(row=0, column=1, padx=8, pady=8)

        tk.Label(self, text="Password").grid(row=1, column=0, padx=8, pady=8)
        self.password = tk.Entry(self, show="*")
        self.password.grid(row=1, column=1, padx=8, pady=8)

        self.login_btn = tk.Button(self, text="Login", command=self.login)
        self.login_btn.grid(row=2, column=0, columnspan=2, pady=10)

        apply_default(self.login_btn)

    def login(self):
        user = AuthService.login(self.username.get(), self.password.get())
        if user:
            messagebox.showinfo("Success", f"Welcome {user['username']}")
            self.on_success(user)
            self.destroy()
        else:
            messagebox.showerror("Error", "Invalid credentials")
