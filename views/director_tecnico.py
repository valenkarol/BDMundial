import tkinter as tk
from tkinter import ttk, messagebox

from controllers.director_tecnico_controller import DirectorTecnicoController


class DirectorTecnicoView:

    def __init__(self):

        self.ventana = tk.Toplevel()
        self.ventana.title("CRUD Directores Técnicos")
        self.ventana.geometry("500x450")

        tk.Label(
            self.ventana,
            text="CRUD DIRECTORES TÉCNICOS",
            font=("Arial", 14, "bold")
        ).pack(pady=10)

        # CAMPO NOMBRE
        tk.Label(self.ventana, text="Nombre del Director:").pack(pady=5)

        self.entrada_nombre = tk.Entry(self.ventana, width=40)
        self.entrada_nombre.pack()

        # BOTONES
        tk.Button(
            self.ventana,
            text="Guardar",
            width=20,
            command=self.guardar
        ).pack(pady=5)

        tk.Button(
            self.ventana,
            text="Eliminar seleccionado",
            width=20,
            command=self.eliminar
        ).pack(pady=2)

        # TABLA
        self.tabla = ttk.Treeview(
            self.ventana,
            columns=("ID", "Nombre"),
            show="headings"
        )
        self.tabla.heading("ID",     text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.column("ID",     width=50,  anchor="center")
        self.tabla.column("Nombre", width=300, anchor="w")
        self.tabla.pack(fill="both", expand=True, padx=10, pady=10)

        self.cargar_tabla()

    def guardar(self):

        nombre = self.entrada_nombre.get().strip()

        if not nombre:
            messagebox.showerror("Error", "Escribe el nombre del director.")
            return

        DirectorTecnicoController.insertar_director(nombre)
        messagebox.showinfo("Correcto", f"Director '{nombre}' guardado.")
        self.entrada_nombre.delete(0, tk.END)
        self.cargar_tabla()

    def eliminar(self):

        seleccion = self.tabla.selection()

        if not seleccion:
            messagebox.showwarning("Atención", "Selecciona un director para eliminar.")
            return

        id_director = self.tabla.item(seleccion[0])["values"][0]

        DirectorTecnicoController.eliminar_director(id_director)
        messagebox.showinfo("Correcto", "Director eliminado.")
        self.cargar_tabla()

    def cargar_tabla(self):

        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        directores = DirectorTecnicoController.obtener_directores()

        for d in directores:
            self.tabla.insert("", tk.END, values=d)