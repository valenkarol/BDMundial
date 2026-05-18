import tkinter as tk


class DirectorTecnicoView:

    def __init__(self):

        self.ventana = tk.Toplevel()

        self.ventana.title("Directores Técnicos")

        self.ventana.geometry("500x400")

        tk.Label(
            self.ventana,
            text="CRUD DIRECTORES"
        ).pack(pady=30)