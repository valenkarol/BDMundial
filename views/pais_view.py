import tkinter as tk
from tkinter import ttk, messagebox

from controllers.pais_controller import PaisController


class PaisView:

    def __init__(self):

        self.ventana = tk.Toplevel()

        self.ventana.title("Países")

        self.ventana.geometry("500x500")

        # ─────────────────────────────
        # NOMBRE
        # ─────────────────────────────

        tk.Label(
            self.ventana,
            text="Nombre País"
        ).pack()

        self.nombre = tk.Entry(
            self.ventana,
            width=40
        )

        self.nombre.pack(pady=5)

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

        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")

        self.tabla.pack(
            fill="both",
            expand=True,
            pady=10
        )

        self.cargar()

    # ─────────────────────────────
    # GUARDAR
    # ─────────────────────────────

    def guardar(self):

        nombre = self.nombre.get()

        if nombre == "":
            messagebox.showerror(
                "Error",
                "Ingrese un nombre"
            )
            return

        PaisController.insertar_pais(nombre)

        self.nombre.delete(0, tk.END)

        self.cargar()

    # ─────────────────────────────
    # ELIMINAR
    # ─────────────────────────────

    def eliminar(self):

        seleccion = self.tabla.selection()

        if not seleccion:

            messagebox.showerror(
                "Error",
                "Seleccione un país"
            )
            return

        item = self.tabla.item(seleccion)

        id_pais = item["values"][0]

        PaisController.eliminar_pais(id_pais)

        messagebox.showinfo(
            "Correcto",
            "País eliminado"
        )

        self.cargar()

    # ─────────────────────────────
    # CARGAR
    # ─────────────────────────────

    def cargar(self):

        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        datos = PaisController.obtener_paises()

        for dato in datos:

            self.tabla.insert(
                "",
                tk.END,
                values=dato
            )