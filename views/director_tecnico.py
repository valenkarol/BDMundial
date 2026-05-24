import tkinter as tk
from tkinter import ttk, messagebox

from controllers.director_tecnico_controller import DirectorTecnicoController


class DirectorTecnicoView:

    def __init__(self):

        self.ventana = tk.Toplevel()

        self.ventana.title("CRUD Directores Técnicos")

        self.ventana.geometry("500x450")

        # ─────────────────────────────
        # TÍTULO
        # ─────────────────────────────

        tk.Label(
            self.ventana,
            text="CRUD DIRECTORES TÉCNICOS",
            font=("Arial", 14, "bold")
        ).pack(pady=10)

        # ─────────────────────────────
        # NOMBRE
        # ─────────────────────────────

        tk.Label(
            self.ventana,
            text="Nombre del Director:"
        ).pack(pady=5)

        self.entrada_nombre = tk.Entry(
            self.ventana,
            width=40
        )

        self.entrada_nombre.pack()

        # ─────────────────────────────
        # BOTONES
        # ─────────────────────────────

        frame_botones = tk.Frame(self.ventana)
        frame_botones.pack(pady=10)

        tk.Button(
            frame_botones,
            text="Guardar",
            width=15,
            command=self.guardar
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
            columns=("ID", "Nombre"),
            show="headings"
        )

        self.tabla.heading(
            "ID",
            text="ID"
        )

        self.tabla.heading(
            "Nombre",
            text="Nombre"
        )

        self.tabla.column(
            "ID",
            width=50,
            anchor="center"
        )

        self.tabla.column(
            "Nombre",
            width=300,
            anchor="w"
        )

        self.tabla.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.cargar_tabla()

    # ─────────────────────────────
    # GUARDAR
    # ─────────────────────────────

    def guardar(self):

        nombre = self.entrada_nombre.get().strip()

        if not nombre:

            messagebox.showerror(
                "Error",
                "Escribe el nombre del director."
            )

            return

        DirectorTecnicoController.insertar_director(
            nombre
        )

        messagebox.showinfo(
            "Correcto",
            f"Director '{nombre}' guardado."
        )

        self.entrada_nombre.delete(0, tk.END)

        self.cargar_tabla()

    # ─────────────────────────────
    # ELIMINAR
    # ─────────────────────────────

    def eliminar(self):

        seleccion = self.tabla.selection()

        if not seleccion:

            messagebox.showwarning(
                "Atención",
                "Selecciona un director para eliminar."
            )

            return

        item = self.tabla.item(
            seleccion[0]
        )

        id_director = item["values"][0]

        DirectorTecnicoController.eliminar_director(
            id_director
        )

        messagebox.showinfo(
            "Correcto",
            "Director eliminado."
        )

        self.cargar_tabla()

    # ─────────────────────────────
    # CARGAR TABLA
    # ─────────────────────────────

    def cargar_tabla(self):

        for fila in self.tabla.get_children():

            self.tabla.delete(fila)

        directores = DirectorTecnicoController.obtener_directores()

        for d in directores:

            self.tabla.insert(
                "",
                tk.END,
                values=d
            )