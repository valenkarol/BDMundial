import tkinter as tk


class JugadorView:

    def __init__(self):

        self.ventana = tk.Toplevel()

        self.ventana.title("Jugadores")

        self.ventana.geometry("500x400")

        tk.Label(
            self.ventana,
            text="CRUD JUGADORES"
        ).pack(pady=30)