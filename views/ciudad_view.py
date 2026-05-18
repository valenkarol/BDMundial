import tkinter as tk
from tkinter import ttk

from controllers.ciudad_controller import CiudadController
from controllers.pais_controller import PaisController


class CiudadView:

    def __init__(self):

        self.ventana = tk.Toplevel()

        self.ventana.title("Ciudades")

        self.ventana.geometry("600x500")

        tk.Label(
            self.ventana,
            text="Nombre Ciudad"
        ).pack()

        self.nombre = tk.Entry(
            self.ventana
        )

        self.nombre.pack()

        tk.Label(
            self.ventana,
            text="País"
        ).pack()

        self.combo_pais = ttk.Combobox(
            self.ventana
        )

        self.combo_pais.pack()

        self.cargar_paises()

        tk.Button(
            self.ventana,
            text="Guardar",
            command=self.guardar
        ).pack(pady=10)

        self.tabla = ttk.Treeview(
            self.ventana,
            columns=("ID", "Ciudad", "País"),
            show="headings"
        )

        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Ciudad", text="Ciudad")
        self.tabla.heading("País", text="País")

        self.tabla.pack(fill="both", expand=True)

        self.cargar_ciudades()

    def cargar_paises(self):

        paises = PaisController.obtener_paises()

        self.paises_dict = {}

        nombres = []

        for pais in paises:

            self.paises_dict[pais[1]] = pais[0]

            nombres.append(pais[1])

        self.combo_pais["values"] = nombres

    def guardar(self):

        nombre = self.nombre.get()

        pais_nombre = self.combo_pais.get()

        id_pais = self.paises_dict[pais_nombre]

        CiudadController.insertar_ciudad(
            nombre,
            id_pais
        )

        self.cargar_ciudades()

    def cargar_ciudades(self):

        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        ciudades = CiudadController.obtener_ciudades()

        for ciudad in ciudades:

            self.tabla.insert(
                "",
                tk.END,
                values=ciudad
            )