import tkinter as tk


class ConfederacionView:

    def __init__(self):

        self.ventana = tk.Toplevel()

        self.ventana.title("Confederaciones")

        self.ventana.geometry("500x400")

        tk.Label(
            self.ventana,
            text="CRUD CONFEDERACIONES"
        ).pack(pady=30)