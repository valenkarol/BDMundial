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

        # ─────────────────────────────
        # NOMBRE
        # ─────────────────────────────

        tk.Label(
            self.ventana,
            text="Nombre Ciudad"
        ).pack(pady=5)

        self.nombre = tk.Entry(
            self.ventana,
            width=40
        )

        self.nombre.pack()

        # ─────────────────────────────
        # PAÍS
        # ─────────────────────────────

        tk.Label(
            self.ventana,
            text="País"
        ).pack(pady=5)

        self.combo_pais = ttk.Combobox(
            self.ventana,
            width=37,
            state="readonly"
        )

        self.combo_pais.pack()

        self.cargar_paises()

        # ─────────────────────────────
        # BOTONES
        # ─────────────────────────────

        frame_botones = tk.Frame(self.ventana)
        frame_botones.pack(pady=10)

        tk.Button(
            frame_botones,
            text="Guardar",
            width=15,
            command=self.guardar_ciudad
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            frame_botones,
            text="Eliminar",
            width=15,
            bg="red",
            fg="white",
            command=self.eliminar
        ).grid(row=0, column=1, padx=5)

        # ─────────────────────────────
        # TABLA
        # ─────────────────────────────

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

    # ─────────────────────────────
    # CARGAR PAÍSES
    # ─────────────────────────────

    def cargar_paises(self):

        paises = PaisController.obtener_paises()

        self.paises_dict = {}

        nombres = []

        for pais in paises:

            self.paises_dict[pais[1]] = pais[0]

            nombres.append(pais[1])

        self.combo_pais["values"] = nombres

    # ─────────────────────────────
    # GUARDAR
    # ─────────────────────────────

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

    # ─────────────────────────────
    # ELIMINAR
    # ─────────────────────────────

    def eliminar(self):

        seleccion = self.tabla.selection()

        if not seleccion:

            messagebox.showerror(
                "Error",
                "Seleccione una ciudad"
            )

            return

        item = self.tabla.item(seleccion)

        id_ciudad = item["values"][0]

        CiudadController.eliminar_ciudad(id_ciudad)

        messagebox.showinfo(
            "Correcto",
            "Ciudad eliminada"
        )

        self.cargar_ciudades()

    # ─────────────────────────────
    # CARGAR TABLA
    # ─────────────────────────────

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