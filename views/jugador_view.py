import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from controllers.jugador_controller import JugadorController
from controllers.equipo_controller import EquipoController


class JugadorView:

    def __init__(self):

        self.ventana = tk.Toplevel()

        self.ventana.title("CRUD JUGADORES")

        self.ventana.geometry("1000x700")

        # CAMPOS
        self.crear_campos()

        # TABLA
        self.crear_tabla()

        self.cargar_equipos()

        self.cargar_jugadores()

    def crear_campos(self):

        labels = [
            "Nombre",
            "Posición",
            "Número",
            "Valor",
            "Edad",
            "Peso",
            "Estatura"
        ]

        self.entries = {}

        for texto in labels:

            tk.Label(
                self.ventana,
                text=texto
            ).pack()

            entry = tk.Entry(
                self.ventana,
                width=40
            )

            entry.pack()

            self.entries[texto] = entry

        # EQUIPO
        tk.Label(
            self.ventana,
            text="Equipo"
        ).pack()

        self.combo_equipo = ttk.Combobox(
            self.ventana,
            state="readonly"
        )

        self.combo_equipo.pack()

        tk.Button(
            self.ventana,
            text="Guardar",
            command=self.guardar_jugador
        ).pack(pady=10)

    def crear_tabla(self):

        columnas = (
            "ID",
            "Nombre",
            "Posición",
            "Número",
            "Valor",
            "Equipo"
        )

        self.tabla = ttk.Treeview(
            self.ventana,
            columns=columnas,
            show="headings"
        )

        for col in columnas:

            self.tabla.heading(
                col,
                text=col
            )

        self.tabla.pack(
            fill="both",
            expand=True
        )

    def cargar_equipos(self):

        equipos = EquipoController.obtener_equipos()

        self.equipos_dict = {}

        nombres = []

        for e in equipos:

            self.equipos_dict[e[1]] = e[0]

            nombres.append(e[1])

        self.combo_equipo["values"] = nombres

    def guardar_jugador(self):

        try:

            nombre = self.entries["Nombre"].get()

            posicion = self.entries["Posición"].get()

            numero = int(
                self.entries["Número"].get()
            )

            valor = float(
                self.entries["Valor"].get()
            )

            edad = int(
                self.entries["Edad"].get()
            )

            peso = float(
                self.entries["Peso"].get()
            )

            estatura = float(
                self.entries["Estatura"].get()
            )

            equipo = self.combo_equipo.get()

            id_equipo = self.equipos_dict[equipo]

            JugadorController.insertar_jugador(
                nombre,
                posicion,
                numero,
                valor,
                edad,
                peso,
                estatura,
                id_equipo
            )

            messagebox.showinfo(
                "Correcto",
                "Jugador guardado"
            )

            self.cargar_jugadores()

        except:

            messagebox.showerror(
                "Error",
                "Datos inválidos"
            )

    def cargar_jugadores(self):

        for fila in self.tabla.get_children():

            self.tabla.delete(fila)

        jugadores = JugadorController.obtener_jugadores()

        for jugador in jugadores:

            self.tabla.insert(
                "",
                tk.END,
                values=jugador
            )