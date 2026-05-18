import tkinter as tk


class EquipoView:

    def __init__(self):

        self.ventana = tk.Toplevel()

        self.ventana.title("Equipos")

        self.ventana.geometry("500x400")

        tk.Label(
            self.ventana,
            text="CRUD EQUIPOS"
        ).pack(pady=30)