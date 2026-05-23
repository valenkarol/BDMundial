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
        self.nombre = usuario[1]
        self.rol = usuario[3]

        self.ventana = tk.Tk()
        self.ventana.title("Sistema Mundial 2026")
        self.ventana.geometry("500x700")
        self.ventana.resizable(False, True)

        # ─────────────────────────────────────────────
        # CONTENEDOR PRINCIPAL CON SCROLL
        # ─────────────────────────────────────────────

        contenedor = tk.Frame(self.ventana)
        contenedor.pack(fill="both", expand=True)

        canvas = tk.Canvas(contenedor)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(
            contenedor,
            orient="vertical",
            command=canvas.yview
        )
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        # Frame interno
        self.frame_menu = tk.Frame(canvas)

        canvas.create_window(
            (0, 0),
            window=self.frame_menu,
            anchor="nw"
        )

        # Actualizar scroll automáticamente
        self.frame_menu.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        # Scroll con rueda del mouse
        canvas.bind_all(
            "<MouseWheel>",
            lambda e: canvas.yview_scroll(
                int(-1 * (e.delta / 120)),
                "units"
            )
        )

        # Registrar salida al cerrar ventana
        self.ventana.protocol(
            "WM_DELETE_WINDOW",
            self.salir
        )

        # ─────────────────────────────────────────────
        # TÍTULO
        # ─────────────────────────────────────────────

        tk.Label(
            self.frame_menu,
            text="MENÚ PRINCIPAL",
            font=("Arial", 20, "bold")
        ).pack(pady=10)

        tk.Label(
            self.frame_menu,
            text=f"Usuario: {self.nombre}   |   Rol: {self.rol}",
            font=("Arial", 10),
            fg="gray"
        ).pack(pady=2)

        tk.Frame(
            self.frame_menu,
            height=2,
            bg="gray"
        ).pack(fill="x", padx=20, pady=8)

        # ─────────────────────────────────────────────
        # SECCIÓN CRUD
        # ─────────────────────────────────────────────

        if self.rol in ("ADMIN", "TRADICIONAL"):

            tk.Label(
                self.frame_menu,
                text="Gestión de datos",
                font=("Arial", 10, "italic"),
                fg="#444"
            ).pack(pady=(6, 2))

            tk.Button(
                self.frame_menu,
                text="Directores Técnicos",
                width=35,
                height=2,
                command=self.abrir_directores
            ).pack(pady=3)

            tk.Button(
                self.frame_menu,
                text="Países",
                width=35,
                height=2,
                command=self.abrir_paises
            ).pack(pady=3)

            tk.Button(
                self.frame_menu,
                text="Ciudades",
                width=35,
                height=2,
                command=self.abrir_ciudades
            ).pack(pady=3)

            tk.Button(
                self.frame_menu,
                text="Estadios",
                width=35,
                height=2,
                command=self.abrir_estadios
            ).pack(pady=3)

            tk.Button(
                self.frame_menu,
                text="Equipos",
                width=35,
                height=2,
                command=self.abrir_equipos
            ).pack(pady=3)

            tk.Button(
                self.frame_menu,
                text="Jugadores",
                width=35,
                height=2,
                command=self.abrir_jugadores
            ).pack(pady=3)

            tk.Button(
                self.frame_menu,
                text="Partidos",
                width=35,
                height=2,
                command=self.abrir_partidos
            ).pack(pady=3)

            # SOLO ADMIN
            if self.rol == "ADMIN":

                tk.Button(
                    self.frame_menu,
                    text="Usuarios",
                    width=35,
                    height=2,
                    command=self.abrir_usuarios
                ).pack(pady=3)

        # ─────────────────────────────────────────────
        # CONSULTAS
        # ─────────────────────────────────────────────

        tk.Label(
            self.frame_menu,
            text="Consultas",
            font=("Arial", 10, "italic"),
            fg="#444"
        ).pack(pady=(8, 2))

        tk.Button(
            self.frame_menu,
            text="Consultas",
            width=35,
            height=2,
            command=self.abrir_consultas
        ).pack(pady=3)

        # ─────────────────────────────────────────────
        # REPORTES
        # ─────────────────────────────────────────────

        tk.Label(
            self.frame_menu,
            text="Reportes PDF",
            font=("Arial", 10, "italic"),
            fg="#444"
        ).pack(pady=(8, 2))

        tk.Button(
            self.frame_menu,
            text="Reporte Usuarios PDF",
            width=35,
            height=2,
            command=generar_reporte_usuarios
        ).pack(pady=3)

        tk.Button(
            self.frame_menu,
            text="Reporte Valor Equipos",
            width=35,
            height=2,
            command=reporte_valor_equipos
        ).pack(pady=3)

        tk.Button(
            self.frame_menu,
            text="Reporte Jugadores por Filtro",
            width=35,
            height=2,
            command=reporte_jugadores_por_filtro
        ).pack(pady=3)

        tk.Button(
            self.frame_menu,
            text="Reporte Partidos por País Sede",
            width=35,
            height=2,
            command=reporte_partidos_por_pais_anfitrion
        ).pack(pady=3)

        # ─────────────────────────────────────────────
        # BOTÓN SALIR
        # ─────────────────────────────────────────────

        tk.Frame(
            self.frame_menu,
            height=2,
            bg="gray"
        ).pack(fill="x", padx=20, pady=8)

        tk.Button(
            self.frame_menu,
            text="Salir",
            width=35,
            height=2,
            bg="red",
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.salir
        ).pack(pady=10)

        self.ventana.mainloop()

    # ─────────────────────────────────────────────
    # SALIR
    # ─────────────────────────────────────────────

    def salir(self):
        BitacoraController.registrar_salida(self.id_usuario)
        self.ventana.destroy()

    # ─────────────────────────────────────────────
    # MÉTODOS CRUD
    # ─────────────────────────────────────────────

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

    # ─────────────────────────────────────────────
    # CONSULTAS
    # ─────────────────────────────────────────────

    def abrir_consultas(self):
        ConsultaView()