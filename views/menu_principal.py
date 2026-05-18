import tkinter as tk

from views.pais_view import PaisView


class MenuPrincipal:

    def __init__(self):

        self.ventana = tk.Tk()

        self.ventana.title("Menú Principal")

        self.ventana.geometry("500x400")

        tk.Label(
            self.ventana,
            text="Sistema Mundial 2026",
            font=("Arial", 18)
        ).pack(pady=20)

        tk.Button(
            self.ventana,
            text="CRUD País",
            width=20,
            command=self.abrir_paises
        ).pack(pady=10)

        self.ventana.mainloop()

    def abrir_paises(self):

        PaisView()