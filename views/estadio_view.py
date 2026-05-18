import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from controllers.estadio_controller import EstadioController
from controllers.ciudad_controller import CiudadController


class EstadioView:

    def __init__(self):

        self.ventana = tk.Toplevel()

        self.ventana.title("CRUD ESTADIOS")

        self.ventana.geometry("800x500")

        # NOMBRE
        tk.Label(
            self.ventana,
            text="Nombre Estadio"
        ).pack()

        self.nombre = tk.Entry(
            self.ventana,
            width=40
        )

        self.nombre.pack()

        # CAPACIDAD
        tk.Label(
            self.ventana,
            text="Capacidad"
        ).pack()

        self.capacidad = tk.Entry(
            self.ventana,
            width=40
        )

        self.capacidad.pack()

        # CIUDAD
        tk.Label(
            self.ventana,
            text="Ciudad"
        ).pack()

        self.combo_ciudad = ttk.Combobox(
            self.ventana,
            width=37,
            state="readonly"
        )

        self.combo_ciudad.pack()

        self.cargar_ciudades()

        # BOTÓN
        tk.Button(
            self.ventana,
            text="Guardar",
            command=self.guardar_estadio
        ).pack(pady=10)

        # TABLA
        self.tabla = ttk.Treeview(
            self.ventana,
            columns=(
                "ID",
                "Nombre",
                "Capacidad",
                "Ciudad"
            ),
            show="headings"
        )

        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Capacidad", text="Capacidad")
        self.tabla.heading("Ciudad", text="Ciudad")

        self.tabla.pack(
            fill="both",
            expand=True
        )

        self.cargar_estadios()

    def cargar_ciudades(self):

        ciudades = CiudadController.obtener_ciudades()

        self.ciudades_dict = {}

        nombres = []

        for ciudad in ciudades:

            self.ciudades_dict[ciudad[1]] = ciudad[0]

            nombres.append(ciudad[1])

        self.combo_ciudad["values"] = nombres

    def guardar_estadio(self):

        nombre = self.nombre.get()

        capacidad = self.capacidad.get()

        ciudad_nombre = self.combo_ciudad.get()

        if (
            nombre == ""
            or capacidad == ""
            or ciudad_nombre == ""
        ):

            messagebox.showerror(
                "Error",
                "Complete todos los campos"
            )

            return

        id_ciudad = self.ciudades_dict[
            ciudad_nombre
        ]

        EstadioController.insertar_estadio(
            nombre,
            capacidad,
            id_ciudad
        )

        messagebox.showinfo(
            "Correcto",
            "Estadio guardado"
        )

        self.nombre.delete(0, tk.END)

        self.capacidad.delete(0, tk.END)

        self.cargar_estadios()

    def cargar_estadios(self):

        for fila in self.tabla.get_children():

            self.tabla.delete(fila)

        estadios = EstadioController.obtener_estadios()

        for estadio in estadios:

            self.tabla.insert(
                "",
                tk.END,
                values=estadio
            )