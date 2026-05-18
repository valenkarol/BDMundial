import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from controllers.ciudad_controller import CiudadController
from controllers.pais_controller import PaisController


class CiudadView:

    def __init__(self):

        self.ventana = tk.Toplevel()

        self.ventana.title("CRUD CIUDADES")

        self.ventana.geometry("700x500")

        # LABEL
        tk.Label(
            self.ventana,
            text="Nombre Ciudad"
        ).pack(pady=5)

        # ENTRY
        self.nombre = tk.Entry(
            self.ventana,
            width=40
        )

        self.nombre.pack()

        # LABEL
        tk.Label(
            self.ventana,
            text="País"
        ).pack(pady=5)

        # COMBOBOX
        self.combo_pais = ttk.Combobox(
            self.ventana,
            width=37,
            state="readonly"
        )

        self.combo_pais.pack()

        self.cargar_paises()

        # BOTÓN
        tk.Button(
            self.ventana,
            text="Guardar",
            command=self.guardar_ciudad
        ).pack(pady=10)

        # TABLA
        self.tabla = ttk.Treeview(
            self.ventana,
            columns=("ID", "Ciudad", "País"),
            show="headings"
        )

        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Ciudad", text="Ciudad")
        self.tabla.heading("País", text="País")

        self.tabla.pack(
            fill="both",
            expand=True,
            pady=20
        )

        self.cargar_ciudades()

    def cargar_paises(self):

        paises = PaisController.obtener_paises()

        self.paises_dict = {}

        nombres = []

        for pais in paises:

            self.paises_dict[pais[1]] = pais[0]

            nombres.append(pais[1])

        self.combo_pais["values"] = nombres

    def guardar_ciudad(self):

        nombre = self.nombre.get()

        pais_nombre = self.combo_pais.get()

        if nombre == "" or pais_nombre == "":

            messagebox.showerror(
                "Error",
                "Complete todos los campos"
            )

            return

        id_pais = self.paises_dict[pais_nombre]

        CiudadController.insertar_ciudad(
            nombre,
            id_pais
        )

        messagebox.showinfo(
            "Correcto",
            "Ciudad guardada"
        )

        self.nombre.delete(0, tk.END)

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