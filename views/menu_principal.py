import tkinter as tk

from views.pais_view import PaisView
from views.ciudad_view import CiudadView
from views.estadio_view import EstadioView
from views.equipo_view import EquipoView
from views.jugador_view import JugadorView
from views.usuario_view import UsuarioView
from views.partido_view import PartidoView
from views.consulta_view import ConsultaView
from views.director_tecnico import DirectorTecnicoView

from reports.reporte_usuarios import generar_reporte_usuarios
from reports.reportes_profesor import reporte_valor_equipos
from reports.reportes_extras import (
    reporte_jugadores_por_filtro,
    reporte_partidos_por_pais_anfitrion
)

from controllers.bitacora_controller import BitacoraController


class MenuPrincipal:

    def __init__(self, usuario):
        """
        usuario = (id_usuario, nombreUsuario, contrasena, rol)
        """
        self.id_usuario = usuario[0]
        self.nombre     = usuario[1]
        self.rol        = usuario[3]  # 'ADMIN' | 'TRADICIONAL' | 'ESPORADICO'

        self.ventana = tk.Tk()
        self.ventana.title("Sistema Mundial 2026")
        self.ventana.geometry("500x700")
        self.ventana.resizable(False, True)

        # Cerrar con la X también registra salida en bitácora
        self.ventana.protocol("WM_DELETE_WINDOW", self.salir)

        # ── TÍTULO ───────────────────────────────────────────
        tk.Label(
            self.ventana,
            text="MENÚ PRINCIPAL",
            font=("Arial", 20, "bold")
        ).pack(pady=10)

        tk.Label(
            self.ventana,
            text=f"Usuario: {self.nombre}   |   Rol: {self.rol}",
            font=("Arial", 10),
            fg="gray"
        ).pack(pady=2)

        tk.Frame(self.ventana, height=2, bg="gray").pack(fill="x", padx=20, pady=8)

        # ── SECCIÓN CRUD ─────────────────────────────────────
        # Solo ADMIN y TRADICIONAL pueden gestionar datos
        if self.rol in ("ADMIN", "TRADICIONAL"):

            tk.Label(
                self.ventana,
                text="Gestión de datos",
                font=("Arial", 10, "italic"),
                fg="#444"
            ).pack(pady=(6, 2))

            # BOTÓN DIRECTORES TÉCNICOS
            tk.Button(
                self.ventana,
                text="Directores Técnicos",
                width=35,
                height=2,
                command=self.abrir_directores
                ).pack(pady=3)

            # BOTÓN PAÍSES
            tk.Button(
                self.ventana,
                text="CRUD Países",
                width=35,
                height=2,
                command=self.abrir_paises
            ).pack(pady=3)

            # BOTÓN CIUDADES
            tk.Button(
                self.ventana,
                text="CRUD Ciudades",
                width=35,
                height=2,
                command=self.abrir_ciudades
            ).pack(pady=3)

            # BOTÓN ESTADIOS
            tk.Button(
                self.ventana,
                text="CRUD Estadios",
                width=35,
                height=2,
                command=self.abrir_estadios
            ).pack(pady=3)

            # BOTÓN EQUIPOS
            tk.Button(
                self.ventana,
                text="CRUD Equipos",
                width=35,
                height=2,
                command=self.abrir_equipos
            ).pack(pady=3)

            # BOTÓN JUGADORES
            tk.Button(
                self.ventana,
                text="CRUD Jugadores",
                width=35,
                height=2,
                command=self.abrir_jugadores
            ).pack(pady=3)

            # BOTÓN PARTIDOS
            tk.Button(
                self.ventana,
                text="CRUD Partidos",
                width=35,
                height=2,
                command=self.abrir_partidos
            ).pack(pady=3)

            # BOTÓN USUARIOS — solo el ADMIN
            if self.rol == "ADMIN":
                tk.Button(
                    self.ventana,
                    text="CRUD Usuarios",
                    width=35,
                    height=2,
                    command=self.abrir_usuarios
                ).pack(pady=3)

        # ── SECCIÓN CONSULTAS ─────────────────────────────────
        # Todos los roles pueden ejecutar consultas
        tk.Label(
            self.ventana,
            text="Consultas",
            font=("Arial", 10, "italic"),
            fg="#444"
        ).pack(pady=(8, 2))

        # BOTÓN CONSULTAS
        tk.Button(
            self.ventana,
            text="Consultas",
            width=35,
            height=2,
            command=self.abrir_consultas
        ).pack(pady=3)

        # ── SECCIÓN REPORTES ──────────────────────────────────
        # Todos los roles pueden ver reportes
        tk.Label(
            self.ventana,
            text="Reportes PDF",
            font=("Arial", 10, "italic"),
            fg="#444"
        ).pack(pady=(8, 2))

        # BOTÓN REPORTE USUARIOS PDF
        tk.Button(
            self.ventana,
            text="Reporte Usuarios PDF",
            width=35,
            height=2,
            command=generar_reporte_usuarios
        ).pack(pady=3)

        # BOTÓN REPORTE VALOR EQUIPOS
        tk.Button(
            self.ventana,
            text="Reporte Valor Equipos",
            width=35,
            height=2,
            command=reporte_valor_equipos
        ).pack(pady=3)

        # BOTÓN REPORTE JUGADORES
        tk.Button(
            self.ventana,
            text="Reporte Jugadores por Filtro",
            width=35,
            height=2,
            command=reporte_jugadores_por_filtro
        ).pack(pady=3)

        # BOTÓN REPORTE PARTIDOS POR PAÍS
        tk.Button(
            self.ventana,
            text="Reporte Partidos por País Sede",
            width=35,
            height=2,
            command=reporte_partidos_por_pais_anfitrion
        ).pack(pady=3)

        # ── BOTÓN SALIR ───────────────────────────────────────
        tk.Frame(self.ventana, height=2, bg="gray").pack(fill="x", padx=20, pady=8)

        tk.Button(
            self.ventana,
            text="Salir",
            width=35,
            height=2,
            bg="red",
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.salir
        ).pack(pady=10)

        # mainloop() siempre al final, después de TODOS los widgets
        self.ventana.mainloop()

    # ── SALIR ─────────────────────────────────────────────────

    def salir(self):
        BitacoraController.registrar_salida(self.id_usuario)
        self.ventana.destroy()

    # ── MÉTODOS CRUD ──────────────────────────────────────────

    def abrir_paises(self):
        PaisView()

    def abrir_ciudades(self):
        CiudadView()

    def abrir_estadios(self):
        EstadioView()

    def abrir_directores(self):
        DirectorTecnicoView()

    def abrir_equipos(self):
        EquipoView()

    def abrir_jugadores(self):
        JugadorView()

    def abrir_partidos(self):
        PartidoView()

    def abrir_usuarios(self):
        UsuarioView()


    # ── CONSULTAS ─────────────────────────────────────────────

    def abrir_consultas(self):
        ConsultaView()