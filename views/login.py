import tkinter as tk
from tkinter import messagebox
from database.conexion import conectar

class Login:

    def __init__(self):

        self.ventana = tk.Tk()
        self.ventana.title("Login Mundial 2026")
        self.ventana.geometry("400x300")

        tk.Label(self.ventana, text="Usuario").pack()

        self.usuario = tk.Entry(self.ventana)
        self.usuario.pack()

        tk.Label(self.ventana, text="Contraseña").pack()

        self.password = tk.Entry(self.ventana, show="*")
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

        conexion = conectar()
        cursor = conexion.cursor()

        query = """
        SELECT * FROM usuario
        WHERE nombreUsuario=%s
        AND contrasena=%s
        """

        cursor.execute(query, (usuario, password))

        resultado = cursor.fetchone()

        if resultado:
            messagebox.showinfo(
                "Correcto",
                "Bienvenido"
            )
        else:
            messagebox.showerror(
                "Error",
                "Datos incorrectos"
            )