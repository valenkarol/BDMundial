import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

from controllers.partido_controller import PartidoController
from controllers.estadio_controller import EstadioController
from controllers.equipo_controller import EquipoController


class PartidoView:

    def __init__(self):

        self.ventana = tk.Toplevel()

        self.ventana.title("CRUD PARTIDOS")

        self.ventana.geometry("800x600")

        # ─────────────────────────────
        # FECHA
        # ─────────────────────────────

        tk.Label(
            self.ventana,
            text="Fecha"
        ).pack()

        self.fecha = DateEntry(
            self.ventana,
            width=37,
            background="darkblue",
            foreground="white",
            borderwidth=2,
            date_pattern="yyyy-mm-dd"
        )

        self.fecha.pack(pady=3)

        # ─────────────────────────────
        # ESTADIO
        # ─────────────────────────────

        tk.Label(
            self.ventana,
            text="Estadio"
        ).pack()

        self.combo_estadio = ttk.Combobox(
            self.ventana,
            state="readonly",
            width=37
        )

        self.combo_estadio.pack(pady=3)

        # ─────────────────────────────
        # EQUIPO LOCAL
        # ─────────────────────────────

        tk.Label(
            self.ventana,
            text="Equipo Local"
        ).pack()

        self.combo_equipo = ttk.Combobox(
            self.ventana,
            state="readonly",
            width=37
        )

        self.combo_equipo.pack(pady=3)

        # ─────────────────────────────
        # EQUIPO VISITANTE
        # ─────────────────────────────

        tk.Label(
            self.ventana,
            text="Equipo Visitante"
        ).pack()

        self.combo_visitante = ttk.Combobox(
            self.ventana,
            state="readonly",
            width=37
        )

        self.combo_visitante.pack(pady=3)

        # ─────────────────────────────
        # CARGAR DATOS
        # ─────────────────────────────

        self.cargar_datos()

        # ─────────────────────────────
        # BOTONES
        # ─────────────────────────────

        frame_botones = tk.Frame(self.ventana)
        frame_botones.pack(pady=10)

        tk.Button(
            frame_botones,
            text="Guardar",
            width=15,
            command=self.guardar_partido
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
            columns=(
                "ID",
                "Fecha",
                "Estadio",
                "Local",
                "Visitante"
            ),
            show="headings"
        )

        self.tabla.heading(
            "ID",
            text="ID"
        )

        self.tabla.heading(
            "Fecha",
            text="Fecha"
        )

        self.tabla.heading(
            "Estadio",
            text="Estadio"
        )

        self.tabla.heading(
            "Local",
            text="Equipo Local"
        )

        self.tabla.heading(
            "Visitante",
            text="Equipo Visitante"
        )

        self.tabla.pack(
            fill="both",
            expand=True,
            pady=10
        )

        self.cargar_partidos()

    # ─────────────────────────────
    # CARGAR DATOS
    # ─────────────────────────────

    def cargar_datos(self):

        # ESTADIOS
        estadios = EstadioController.obtener_estadios()

        self.estadios_dict = {}

        lista_estadios = []

        for estadio in estadios:

            self.estadios_dict[
                estadio[1]
            ] = estadio[0]

            lista_estadios.append(
                estadio[1]
            )

        self.combo_estadio["values"] = lista_estadios

        # EQUIPOS
        equipos = EquipoController.obtener_equipos()

        self.equipos_dict = {}

        lista_equipos = []

        for equipo in equipos:

            self.equipos_dict[
                equipo[1]
            ] = equipo[0]

            lista_equipos.append(
                equipo[1]
            )

        self.combo_equipo["values"] = lista_equipos

        self.combo_visitante["values"] = lista_equipos

    # ─────────────────────────────
    # GUARDAR
    # ─────────────────────────────

    def guardar_partido(self):

        try:

            fecha = self.fecha.get()

            estadio = self.combo_estadio.get()

            equipo_local = self.combo_equipo.get()

            visitante = self.combo_visitante.get()

            if (
                estadio == ""
                or equipo_local == ""
                or visitante == ""
            ):

                messagebox.showerror(
                    "Error",
                    "Complete todos los campos"
                )

                return

            if equipo_local == visitante:

                messagebox.showerror(
                    "Error",
                    "El equipo local y visitante no pueden ser iguales"
                )

                return

            PartidoController.insertar_partido(
                fecha,
                self.estadios_dict[estadio],
                self.equipos_dict[equipo_local],
                self.equipos_dict[visitante]
            )

            messagebox.showinfo(
                "Correcto",
                "Partido guardado"
            )

            self.cargar_partidos()

        except Exception as e:

            messagebox.showerror(
                "Error SQL",
                str(e)
            )

    # ─────────────────────────────
    # ELIMINAR
    # ─────────────────────────────

    def eliminar(self):

        try:

            seleccion = self.tabla.selection()

            if not seleccion:

                messagebox.showerror(
                    "Error",
                    "Seleccione un partido"
                )

                return

            item = self.tabla.item(seleccion)

            id_partido = item["values"][0]

            PartidoController.eliminar_partido(
                id_partido
            )

            messagebox.showinfo(
                "Correcto",
                "Partido eliminado"
            )

            self.cargar_partidos()

        except Exception as e:

            messagebox.showerror(
                "Error SQL",
                str(e)
            )

    # ─────────────────────────────
    # CARGAR TABLA
    # ─────────────────────────────

    def cargar_partidos(self):

        for fila in self.tabla.get_children():

            self.tabla.delete(fila)

        partidos = PartidoController.obtener_partidos()

        for partido in partidos:

            self.tabla.insert(
                "",
                tk.END,
                values=partido
            )