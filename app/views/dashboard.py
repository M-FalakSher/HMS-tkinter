import tkinter as tk
from tkinter import ttk, messagebox
from app.services.patient_service import PatientService
from app.utils.style import apply_default

class DashboardWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Admin Dashboard")
        self.geometry("720x480")

        # Patients section
        frame = tk.LabelFrame(self, text="Patients")
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(frame, columns=("id","name","phone"), show="headings")
        for col in ("id","name","phone"):
            self.tree.heading(col, text=col.capitalize())
        self.tree.pack(fill="both", expand=True)

        form = tk.Frame(frame)
        form.pack(fill="x", pady=8)
        tk.Label(form, text="Name").grid(row=0, column=0)
        self.name = tk.Entry(form); self.name.grid(row=0, column=1)
        tk.Label(form, text="Phone").grid(row=0, column=2)
        self.phone = tk.Entry(form); self.phone.grid(row=0, column=3)

        btns = tk.Frame(frame); btns.pack(pady=8)
        tk.Button(btns, text="Create", command=self.create_patient).grid(row=0, column=0, padx=5)
        tk.Button(btns, text="Update", command=self.update_patient).grid(row=0, column=1, padx=5)
        tk.Button(btns, text="Delete", command=self.delete_patient).grid(row=0, column=2, padx=5)

        apply_default(self)
        self.refresh()

    def refresh(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for p in PatientService.list_patients() or []:
            self.tree.insert("", "end", values=(p["id"], p["name"], p.get("phone","")))

    def _selected_id(self):
        item = self.tree.selection()
        if not item:
            return None
        return self.tree.item(item[0])["values"][0]

    def create_patient(self):
        try:
            PatientService.create_patient(self.name.get(), phone=self.phone.get())
            self.refresh()
            messagebox.showinfo("Success", "Patient created")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def update_patient(self):
        pid = self._selected_id()
        if not pid:
            messagebox.showwarning("Select", "Please select a patient")
            return
        try:
            PatientService.update_patient(pid, self.name.get(), None, None, self.phone.get(), None)
            self.refresh()
            messagebox.showinfo("Success", "Patient updated")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def delete_patient(self):
        pid = self._selected_id()
        if not pid:
            messagebox.showwarning("Select", "Please select a patient")
            return
        PatientService.delete_patient(pid)
        self.refresh()
        messagebox.showinfo("Deleted", "Patient deleted")
