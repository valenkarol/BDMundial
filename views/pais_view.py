import tkinter as tk
from tkinter import ttk
from controllers.pais_controller import PaisController


class PaisView:

    def __init__(self):

        self.ventana = tk.Toplevel()

        self.ventana.title("Países")

        self.ventana.geometry("500x400")

        tk.Label(
            self.ventana,
            text="Nombre País"
        ).pack()

        self.nombre = tk.Entry(
            self.ventana
        )

        self.nombre.pack()

        tk.Button(
            self.ventana,
            text="Guardar",
            command=self.guardar
        ).pack(pady=10)

        self.tabla = ttk.Treeview(
            self.ventana,
            columns=("ID", "Nombre"),
            show="headings"
        )

        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")

        self.tabla.pack(fill="both", expand=True)

        self.cargar()

    def guardar(self):

        nombre = self.nombre.get()

        PaisController.insertar_pais(nombre)

        self.nombre.delete(0, tk.END)

        self.cargar()

    def cargar(self):

        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        datos = PaisController.obtener_paises()

        for dato in datos:

            self.tabla.insert(
                "",
                tk.END,
                values=dato
            )