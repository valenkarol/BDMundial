import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from controllers.equipo_controller import EquipoController
from controllers.confederacion_controller import ConfederacionController
from controllers.grupo_controller import GrupoController
from controllers.director_tecnico_controller import DirectorTecnicoController


class EquipoView:

    def __init__(self):

        self.ventana = tk.Toplevel()

        self.ventana.title("CRUD EQUIPOS")

        self.ventana.geometry("900x600")

        # NOMBRE
        tk.Label(
            self.ventana,
            text="Nombre Equipo"
        ).pack()

        self.nombre = tk.Entry(
            self.ventana,
            width=40
        )

        self.nombre.pack()

        # CONFEDERACIÓN
        tk.Label(
            self.ventana,
            text="Confederación"
        ).pack()

        self.combo_confederacion = ttk.Combobox(
            self.ventana,
            state="readonly"
        )

        self.combo_confederacion.pack()

        # GRUPO
        tk.Label(
            self.ventana,
            text="Grupo"
        ).pack()

        self.combo_grupo = ttk.Combobox(
            self.ventana,
            state="readonly"
        )

        self.combo_grupo.pack()

        # DIRECTOR
        tk.Label(
            self.ventana,
            text="Director Técnico"
        ).pack()

        self.combo_director = ttk.Combobox(
            self.ventana,
            state="readonly"
        )

        self.combo_director.pack()

        self.cargar_datos()

        tk.Button(
            self.ventana,
            text="Guardar",
            command=self.guardar_equipo
        ).pack(pady=10)

        # TABLA
        self.tabla = ttk.Treeview(
            self.ventana,
            columns=(
                "ID",
                "Equipo",
                "Confederación",
                "Grupo",
                "Director"
            ),
            show="headings"
        )

        for col in (
            "ID",
            "Equipo",
            "Confederación",
            "Grupo",
            "Director"
        ):

            self.tabla.heading(
                col,
                text=col
            )

        self.tabla.pack(
            fill="both",
            expand=True
        )

        self.cargar_equipos()

    def cargar_datos(self):

        # CONFEDERACIONES
        confs = ConfederacionController.obtener_confederaciones()

        self.conf_dict = {}

        lista_conf = []

        for c in confs:

            self.conf_dict[c[1]] = c[0]

            lista_conf.append(c[1])

        self.combo_confederacion["values"] = lista_conf

        # GRUPOS
        grupos = GrupoController.obtener_grupos()

        self.grupo_dict = {}

        lista_grupos = []

        for g in grupos:

            self.grupo_dict[g[1]] = g[0]

            lista_grupos.append(g[1])

        self.combo_grupo["values"] = lista_grupos

        # DIRECTORES
        directores = DirectorTecnicoController.obtener_directores()

        self.director_dict = {}

        lista_directores = []

        for d in directores:

            self.director_dict[d[1]] = d[0]

            lista_directores.append(d[1])

        self.combo_director["values"] = lista_directores

    def guardar_equipo(self):

        nombre = self.nombre.get()

        conf = self.combo_confederacion.get()

        grupo = self.combo_grupo.get()

        director = self.combo_director.get()

        if (
            nombre == ""
            or conf == ""
            or grupo == ""
            or director == ""
        ):

            messagebox.showerror(
                "Error",
                "Complete todos los campos"
            )

            return

        EquipoController.insertar_equipo(
            nombre,
            self.conf_dict[conf],
            self.grupo_dict[grupo],
            self.director_dict[director]
        )

        messagebox.showinfo(
            "Correcto",
            "Equipo guardado"
        )

        self.cargar_equipos()

    def cargar_equipos(self):

        for fila in self.tabla.get_children():

            self.tabla.delete(fila)

        equipos = EquipoController.obtener_equipos()

        for equipo in equipos:

            self.tabla.insert(
                "",
                tk.END,
                values=equipo
            )