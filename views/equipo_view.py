import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from controllers.equipo_controller import EquipoController
from controllers.confederacion_controller import ConfederacionController
from controllers.grupo_controller import GrupoController
from controllers.director_tecnico_controller import DirectorTecnicoController
from controllers.pais_controller import PaisController


class EquipoView:

    def __init__(self):

        self.ventana = tk.Toplevel()

        self.ventana.title("CRUD EQUIPOS")

        self.ventana.geometry("900x600")

        # ─────────────────────────────
        # NOMBRE
        # ─────────────────────────────

        tk.Label(
            self.ventana,
            text="Nombre Equipo"
        ).pack()

        self.nombre = tk.Entry(
            self.ventana,
            width=40
        )

        self.nombre.pack()

        # ─────────────────────────────
        # CONFEDERACIÓN
        # ─────────────────────────────

        tk.Label(
            self.ventana,
            text="Confederación"
        ).pack()

        self.combo_confederacion = ttk.Combobox(
            self.ventana,
            state="readonly"
        )

        self.combo_confederacion.pack()

        # ─────────────────────────────
        # GRUPO
        # ─────────────────────────────

        tk.Label(
            self.ventana,
            text="Grupo"
        ).pack()

        self.combo_grupo = ttk.Combobox(
            self.ventana,
            state="readonly"
        )

        self.combo_grupo.pack()

        # ─────────────────────────────
        # DIRECTOR TÉCNICO
        # ─────────────────────────────

        tk.Label(
            self.ventana,
            text="Director Técnico"
        ).pack()

        self.combo_director = ttk.Combobox(
            self.ventana,
            state="readonly"
        )

        self.combo_director.pack()

        # ─────────────────────────────
        # PAÍS
        # ─────────────────────────────

        tk.Label(
            self.ventana,
            text="País"
        ).pack()

        self.combo_pais = ttk.Combobox(
            self.ventana,
            state="readonly"
        )

        self.combo_pais.pack()

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
            command=self.guardar_equipo
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
            expand=True,
            pady=20
        )

        self.cargar_equipos()

    # ─────────────────────────────
    # CARGAR DATOS
    # ─────────────────────────────

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

        # PAÍSES
        paises = PaisController.obtener_paises()

        self.pais_dict = {}

        lista_paises = []

        for p in paises:

            self.pais_dict[p[1]] = p[0]

            lista_paises.append(p[1])

        self.combo_pais["values"] = lista_paises

    # ─────────────────────────────
    # GUARDAR
    # ─────────────────────────────

    def guardar_equipo(self):

        nombre = self.nombre.get()

        conf = self.combo_confederacion.get()

        grupo = self.combo_grupo.get()

        director = self.combo_director.get()

        pais = self.combo_pais.get()

        if (
            nombre == ""
            or conf == ""
            or grupo == ""
            or director == ""
            or pais == ""
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
            self.director_dict[director],
            self.pais_dict[pais]
        )

        messagebox.showinfo(
            "Correcto",
            "Equipo guardado"
        )

        self.nombre.delete(0, tk.END)

        self.cargar_equipos()

    # ─────────────────────────────
    # ELIMINAR
    # ─────────────────────────────

    def eliminar(self):

        seleccion = self.tabla.selection()

        if not seleccion:

            messagebox.showerror(
                "Error",
                "Seleccione un equipo"
            )

            return

        item = self.tabla.item(seleccion)

        id_equipo = item["values"][0]

        EquipoController.eliminar_equipo(
            id_equipo
        )

        messagebox.showinfo(
            "Correcto",
            "Equipo eliminado"
        )

        self.cargar_equipos()

    # ─────────────────────────────
    # CARGAR TABLA
    # ─────────────────────────────

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