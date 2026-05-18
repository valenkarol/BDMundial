import tkinter as tk


class EstadioView:

    def __init__(self):

        self.ventana = tk.Toplevel()

        self.ventana.title("Estadios")

        self.ventana.geometry("500x400")

        tk.Label(
            self.ventana,
            text="CRUD ESTADIOS"
        ).pack(pady=30)