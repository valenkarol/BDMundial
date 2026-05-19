import tkinter as tk
 
from views.pais_view import PaisView
from views.ciudad_view import CiudadView
from views.estadio_view import EstadioView
from views.equipo_view import EquipoView
from views.jugador_view import JugadorView
from views.usuario_view import UsuarioView
from views.partido_view import PartidoView
 
from reports.reporte_usuarios import generar_reporte_usuarios
from reports.reportes_profesor import reporte_valor_equipos
from controllers.bitacora_controller import BitacoraController
from views.consulta_view import ConsultaView

from reports.reportes_extras import (
    reporte_jugadores_por_filtro,
    reporte_partidos_por_pais_anfitrion
)
 
 
class MenuPrincipal:
 
    def __init__(self, usuario):
        """
        usuario = tupla completa devuelta por el login:
        (id_usuario, nombreUsuario, contrasena, rol)
        """
        self.id_usuario = usuario[0]
 
        self.ventana = tk.Tk()
        self.ventana.title("Sistema Mundial 2026")
        self.ventana.geometry("500x650")
 
        # Registrar salida cuando el usuario cierre la ventana
        self.ventana.protocol("WM_DELETE_WINDOW", self.salir)
 
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
 
        # BOTÓN REPORTE USUARIOS PDF
        tk.Button(
            self.ventana,
            text="Reporte Usuarios PDF",
            width=30,
            height=2,
            command=generar_reporte_usuarios
        ).pack(pady=5)
 
        # CORREGIDO: este botón estaba después de mainloop() y nunca aparecía
        tk.Button(
            self.ventana,
            text="Reporte Valor Equipos",
            width=30,
            height=2,
            command=reporte_valor_equipos
        ).pack(pady=5)

        # BOTOS REPORTE JUGADORES
        tk.Button(
               self.ventana,
               text="Reporte Jugadores por Filtro",
               width=30, height=2,
               command=reporte_jugadores_por_filtro
        ).pack(pady=5)

        # BOTOS REPORTE PAARTIDOS POR PAIS
        tk.Button(
            self.ventana,
            text="Reporte Partidos por País Sede",
            width=30, height=2,
            command=reporte_partidos_por_pais_anfitrion
            ).pack(pady=5)
 
        # BOTÓN SALIR
        tk.Button(
            self.ventana,
            text="Salir",
            width=30,
            height=2,
            bg="red",
            fg="white",
            command=self.salir   # CORREGIDO: llama a salir() en lugar de destroy directo
        ).pack(pady=10)

        # BOTÓN CONSULTAS
        tk.Button(
            self.ventana,
            text="Consultas",
            width=30,
            height=2,
            command=self.abrir_consultas
        ).pack(pady=5)
 
        # mainloop() siempre al final, después de todos los widgets
        self.ventana.mainloop()
 
    def salir(self):
        # Registra la salida en la bitácora antes de cerrar
        BitacoraController.registrar_salida(self.id_usuario)
        self.ventana.destroy()
 
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

    def abrir_consultas(self):
        ConsultaView()