import tkinter as tk
from tkinter import messagebox

from controllers.login_controller import LoginController
from views.menu_principal import MenuPrincipal


class Login:

    def __init__(self):

        self.ventana = tk.Tk()

        self.ventana.title("Login Mundial 2026")

        self.ventana.geometry("400x300")

        tk.Label(
            self.ventana,
            text="Usuario"
        ).pack(pady=10)

        self.usuario = tk.Entry(
            self.ventana
        )

        self.usuario.pack()

        tk.Label(
            self.ventana,
            text="Contraseña"
        ).pack(pady=10)

        self.password = tk.Entry(
            self.ventana,
            show="*"
        )

        self.password.pack()

        tk.Button(
            self.ventana,
            text="Ingresar",
            command=self.login
        ).pack(pady=20)

        self.ventana.mainloop()

    def login(self):

        usuario = self.usuario.get()

        password = self.password.get()

        resultado = LoginController.validar_usuario(
            usuario,
            password
        )

        if resultado:

            messagebox.showinfo(
                "Correcto",
                "Bienvenido"
            )

            self.ventana.destroy()

            MenuPrincipal()

        else:

            messagebox.showerror(
                "Error",
                "Usuario incorrecto"
            )