import tkinter as tk


class PartidoView:

    def __init__(self):

        self.ventana = tk.Toplevel()

        self.ventana.title("Partidos")

        self.ventana.geometry("500x400")

        tk.Label(
            self.ventana,
            text="CRUD PARTIDOS"
        ).pack(pady=30)