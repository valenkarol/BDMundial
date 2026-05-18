import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from controllers.pais_controller import PaisController


class PaisView:

    def __init__(self):

        self.ventana = tk.Toplevel()

        self.ventana.title("CRUD País")

        self.ventana.geometry("600x500")

        # LABEL
        tk.Label(
            self.ventana,
            text="Nombre País"
        ).pack(pady=10)

        # INPUT
        self.nombre = tk.Entry(
            self.ventana,
            width=40
        )

        self.nombre.pack()

        # BOTON GUARDAR
        tk.Button(
            self.ventana,
            text="Guardar",
            command=self.guardar_pais
        ).pack(pady=10)

        # TABLA
        self.tabla = ttk.Treeview(
            self.ventana,
            columns=("ID", "Nombre"),
            show="headings"
        )

        self.tabla.heading("ID", text="ID")

        self.tabla.heading("Nombre", text="Nombre")

        self.tabla.pack(pady=20)

        # BOTON ELIMINAR
        tk.Button(
            self.ventana,
            text="Eliminar",
            command=self.eliminar_pais
        ).pack(pady=10)

        self.cargar_paises()

    def guardar_pais(self):

        nombre = self.nombre.get()

        if nombre == "":

            messagebox.showerror(
                "Error",
                "Ingrese un nombre"
            )

            return

        PaisController.insertar_pais(nombre)

        self.nombre.delete(0, tk.END)

        self.cargar_paises()

    def cargar_paises(self):

        for fila in self.tabla.get_children():

            self.tabla.delete(fila)

        paises = PaisController.obtener_paises()

        for pais in paises:

            self.tabla.insert(
                "",
                tk.END,
                values=pais
            )

    def eliminar_pais(self):

        seleccion = self.tabla.selection()

        if not seleccion:

            messagebox.showerror(
                "Error",
                "Seleccione un país"
            )

            return

        datos = self.tabla.item(seleccion)

        id_pais = datos["values"][0]

        PaisController.eliminar_pais(id_pais)

        self.cargar_paises()