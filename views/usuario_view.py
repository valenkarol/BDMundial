import tkinter as tk


class UsuarioView:

    def __init__(self):

        self.ventana = tk.Toplevel()

        self.ventana.title("Usuarios")

        self.ventana.geometry("500x400")

        tk.Label(
            self.ventana,
            text="CRUD USUARIOS"
        ).pack(pady=30)