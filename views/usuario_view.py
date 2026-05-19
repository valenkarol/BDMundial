import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from controllers.usuario_controller import UsuarioController


class UsuarioView:

    def __init__(self):

        self.ventana = tk.Toplevel()

        self.ventana.title("CRUD USUARIOS")

        self.ventana.geometry("700x500")

        # USUARIO
        tk.Label(
            self.ventana,
            text="Usuario"
        ).pack()

        self.usuario = tk.Entry(
            self.ventana,
            width=40
        )

        self.usuario.pack()

        # PASSWORD
        tk.Label(
            self.ventana,
            text="Contraseña"
        ).pack()

        self.password = tk.Entry(
            self.ventana,
            width=40,
            show="*"
        )

        self.password.pack()

        # ROL
        tk.Label(
            self.ventana,
            text="Rol"
        ).pack()

        self.combo_rol = ttk.Combobox(
            self.ventana,
            state="readonly",
            values=[
                "ADMIN",
                "TRADICIONAL",
                "ESPORADICO"
            ]
        )

        self.combo_rol.pack()

        # BOTÓN
        tk.Button(
            self.ventana,
            text="Guardar",
            command=self.guardar_usuario
        ).pack(pady=10)

        # TABLA
        self.tabla = ttk.Treeview(
            self.ventana,
            columns=(
                "ID",
                "Usuario",
                "Contraseña",
                "Rol"
            ),
            show="headings"
        )

        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Usuario", text="Usuario")
        self.tabla.heading("Contraseña", text="Contraseña")
        self.tabla.heading("Rol", text="Rol")

        self.tabla.pack(
            fill="both",
            expand=True
        )

        self.cargar_usuarios()

    def guardar_usuario(self):

        usuario = self.usuario.get()

        password = self.password.get()

        rol = self.combo_rol.get()

        if (
            usuario == ""
            or password == ""
            or rol == ""
        ):

            messagebox.showerror(
                "Error",
                "Complete todos los campos"
            )

            return

        UsuarioController.insertar_usuario(
            usuario,
            password,
            rol
        )

        messagebox.showinfo(
            "Correcto",
            "Usuario guardado"
        )

        self.usuario.delete(0, tk.END)

        self.password.delete(0, tk.END)

        self.cargar_usuarios()

    def cargar_usuarios(self):

        for fila in self.tabla.get_children():

            self.tabla.delete(fila)

        usuarios = UsuarioController.obtener_usuarios()

        for usuario in usuarios:

            self.tabla.insert(
                "",
                tk.END,
                values=usuario
            )