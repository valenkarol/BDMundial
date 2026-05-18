import tkinter as tk

from views.pais_view import PaisView
from views.ciudad_view import CiudadView
from views.estadio_view import EstadioView
from views.equipo_view import EquipoView
from views.jugador_view import JugadorView
from views.usuario_view import UsuarioView

from reports.reporte_usuarios import generar_reporte_usuarios

class MenuPrincipal:

    def __init__(self):

        self.ventana = tk.Tk()

        self.ventana.title("Sistema Mundial 2026")

        self.ventana.geometry("500x500")

        tk.Label(
            self.ventana,
            text="MENÚ PRINCIPAL",
            font=("Arial", 18)
        ).pack(pady=20)

        tk.Button(
            self.ventana,
            text="Países",
            width=25,
            command=self.abrir_paises
        ).pack(pady=5)

        tk.Button(
            self.ventana,
            text="Ciudades",
            width=25,
            command=self.abrir_ciudades
        ).pack(pady=5)

        tk.Button(
            self.ventana,
            text="Estadios",
            width=25,
            command=self.abrir_estadios
        ).pack(pady=5)

        tk.Button(
            self.ventana,
            text="Equipos",
            width=25,
            command=self.abrir_equipos
        ).pack(pady=5)

        tk.Button(
            self.ventana,
            text="Jugadores",
            width=25,
            command=self.abrir_jugadores
        ).pack(pady=5)

        tk.Button(
            self.ventana,
            text="Usuarios",
            width=25,
            command=self.abrir_usuarios
        ).pack(pady=5)

        tk.Button(
    self.ventana,
    text="Reporte Usuarios PDF",
    width=25,
    command=generar_reporte_usuarios
).pack(pady=5)

        self.ventana.mainloop()

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

    def abrir_usuarios(self):
        UsuarioView()