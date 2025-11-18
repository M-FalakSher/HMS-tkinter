import tkinter as tk
from app.views.login import LoginWindow
from app.views.dashboard import DashboardWindow
from app.views.billing import BillingWindow

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hospital Management System")
        self.geometry("960x600")
        self.user = None

        def on_login(user):
            self.user = user
            self.render_main()

        LoginWindow(self, on_success=on_login)

    def render_main(self):
        menu = tk.Menu(self)
        self.config(menu=menu)

        admin_menu = tk.Menu(menu, tearoff=0)
        admin_menu.add_command(label="Dashboard", command=lambda: DashboardWindow(self))
        admin_menu.add_command(label="Billing", command=lambda: BillingWindow(self))
        menu.add_cascade(label="Admin", menu=admin_menu)

if __name__ == "__main__":
    App().mainloop()
