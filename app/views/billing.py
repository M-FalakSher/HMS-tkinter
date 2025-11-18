import tkinter as tk
from tkinter import ttk, messagebox
from app.services.billing_service import BillingService

class BillingWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Billing & Payments")
        self.geometry("640x420")

        self.tree = ttk.Treeview(self, columns=("id","appointment_id","amount","status"), show="headings")
        for col in ("id","appointment_id","amount","status"):
            self.tree.heading(col, text=col.capitalize())
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        form = tk.Frame(self); form.pack(fill="x", padx=10)
        tk.Label(form, text="Appointment ID").grid(row=0, column=0)
        self.app_id = tk.Entry(form); self.app_id.grid(row=0, column=1)
        tk.Label(form, text="Amount").grid(row=0, column=2)
        self.amount = tk.Entry(form); self.amount.grid(row=0, column=3)

        btns = tk.Frame(self); btns.pack(pady=8)
        tk.Button(btns, text="Create Bill", command=self.create_bill).grid(row=0, column=0, padx=5)
        tk.Button(btns, text="Mark Paid", command=self.mark_paid).grid(row=0, column=1, padx=5)
        tk.Button(btns, text="Delete Bill", command=self.delete_bill).grid(row=0, column=2, padx=5)

        self.refresh()

    def refresh(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for b in BillingService.list_bills() or []:
            self.tree.insert("", "end", values=(b["id"], b["appointment_id"], b["amount"], b["status"]))

    def _selected_id(self):
        item = self.tree.selection()
        if not item:
            return None
        return self.tree.item(item[0])["values"][0]

    def create_bill(self):
        try:
            BillingService.create_bill(int(self.app_id.get()), float(self.amount.get()))
            self.refresh()
            messagebox.showinfo("Success", "Bill created")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def mark_paid(self):
        bid = self._selected_id()
        if not bid: return
        BillingService.mark_paid(bid)
        self.refresh()

    def delete_bill(self):
        bid = self._selected_id()
        if not bid: return
        BillingService.delete_bill(bid)
        self.refresh()
