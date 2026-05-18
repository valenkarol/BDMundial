import tkinter as tk


class GrupoView:

    def __init__(self):

        self.ventana = tk.Toplevel()

        self.ventana.title("Grupos")

        self.ventana.geometry("500x400")

        tk.Label(
            self.ventana,
            text="CRUD GRUPOS"
        ).pack(pady=30)