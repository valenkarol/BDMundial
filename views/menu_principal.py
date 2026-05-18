import tkinter as tk

from views.pais_view import PaisView
from views.ciudad_view import CiudadView
from views.estadio_view import EstadioView
from views.equipo_view import EquipoView
from views.jugador_view import JugadorView
from views.usuario_view import UsuarioView
from views.partido_view import PartidoView

from reports.reporte_usuarios import generar_reporte_usuarios


class MenuPrincipal:

    def __init__(self):

        self.ventana = tk.Tk()

        self.ventana.title("Sistema Mundial 2026")

        self.ventana.geometry("500x650")

        # TÍTULO
        tk.Label(
            self.ventana,
            text="MENÚ PRINCIPAL",
            font=("Arial", 20)
        ).pack(pady=20)

        # BOTÓN PAÍSES
        tk.Button(
            self.ventana,
            text="CRUD Países",
            width=30,
            height=2,
            command=self.abrir_paises
        ).pack(pady=5)

        # BOTÓN CIUDADES
        tk.Button(
            self.ventana,
            text="CRUD Ciudades",
            width=30,
            height=2,
            command=self.abrir_ciudades
        ).pack(pady=5)

        # BOTÓN ESTADIOS
        tk.Button(
            self.ventana,
            text="CRUD Estadios",
            width=30,
            height=2,
            command=self.abrir_estadios
        ).pack(pady=5)

        # BOTÓN EQUIPOS
        tk.Button(
            self.ventana,
            text="CRUD Equipos",
            width=30,
            height=2,
            command=self.abrir_equipos
        ).pack(pady=5)

        # BOTÓN JUGADORES
        tk.Button(
            self.ventana,
            text="CRUD Jugadores",
            width=30,
            height=2,
            command=self.abrir_jugadores
        ).pack(pady=5)

        # BOTÓN PARTIDOS
        tk.Button(
            self.ventana,
            text="CRUD Partidos",
            width=30,
            height=2,
            command=self.abrir_partidos
        ).pack(pady=5)

        # BOTÓN USUARIOS
        tk.Button(
            self.ventana,
            text="CRUD Usuarios",
            width=30,
            height=2,
            command=self.abrir_usuarios
        ).pack(pady=5)

        # BOTÓN REPORTE PDF
        tk.Button(
            self.ventana,
            text="Reporte Usuarios PDF",
            width=30,
            height=2,
            command=generar_reporte_usuarios
        ).pack(pady=15)

        # BOTÓN SALIR
        tk.Button(
            self.ventana,
            text="Salir",
            width=30,
            height=2,
            bg="red",
            fg="white",
            command=self.ventana.destroy
        ).pack(pady=10)

        self.ventana.mainloop()

    # MÉTODOS

    def abrir_paises(self):
        PaisView()

    def abrir_ciudades(self):
        CiudadView()

    def abrir_estadios(self):
        EstadioView()

    def abrir_equipos(self):
        EquipoView()

    def abrir_jugadores(self):
        JugadorView()

    def abrir_partidos(self):
        PartidoView()

    def abrir_usuarios(self):
        UsuarioView()