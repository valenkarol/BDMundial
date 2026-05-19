import tkinter as tk
from tkinter import ttk, messagebox

from controllers.consulta_controller import ConsultaController


class ConsultaView:

    def __init__(self):

        self.ventana = tk.Tk()
        self.ventana.title("Consultas — Mundial 2026")
        self.ventana.geometry("700x550")

        tk.Label(
            self.ventana,
            text="CONSULTAS",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        # ── 4 botones, uno por consulta ──────────────────────
        tk.Button(
            self.ventana,
            text="1. Jugador más costoso por confederación",
            width=50, height=2,
            command=self.consulta_1
        ).pack(pady=4)

        tk.Button(
            self.ventana,
            text="2. Partidos por estadio",
            width=50, height=2,
            command=self.consulta_2
        ).pack(pady=4)

        tk.Button(
            self.ventana,
            text="3. Equipo más costoso por país anfitrión",
            width=50, height=2,
            command=self.consulta_3
        ).pack(pady=4)

        tk.Button(
            self.ventana,
            text="4. Jugadores menores de 21 años por equipo",
            width=50, height=2,
            command=self.consulta_4
        ).pack(pady=4)

        # ── Tabla de resultados ──────────────────────────────
        frame = tk.Frame(self.ventana)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        scroll_y = tk.Scrollbar(frame, orient="vertical")
        scroll_x = tk.Scrollbar(frame, orient="horizontal")

        self.tabla = ttk.Treeview(
            frame,
            yscrollcommand=scroll_y.set,
            xscrollcommand=scroll_x.set
        )

        scroll_y.config(command=self.tabla.yview)
        scroll_x.config(command=self.tabla.xview)

        scroll_y.pack(side="right",  fill="y")
        scroll_x.pack(side="bottom", fill="x")
        self.tabla.pack(fill="both", expand=True)

        self.ventana.mainloop()

    # ── Método auxiliar para llenar la tabla ────────────────
    def _mostrar(self, columnas, filas):
        """Limpia la tabla y muestra nuevos resultados."""

        self.tabla.delete(*self.tabla.get_children())

        self.tabla["columns"] = columnas
        self.tabla["show"]    = "headings"

        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=160, anchor="center")

        for fila in filas:
            self.tabla.insert("", "end", values=fila)

    # ── CONSULTA 1 ───────────────────────────────────────────
    def consulta_1(self):

        datos = ConsultaController.jugador_mas_costoso_por_confederacion()

        if not datos:
            messagebox.showinfo("Sin resultados", "No hay datos.")
            return

        self._mostrar(
            ("Confederación", "Jugador", "Valor (€)"),
            datos
        )

    # ── CONSULTA 2 ───────────────────────────────────────────
    def consulta_2(self):
        """Abre ventana para elegir estadio y muestra sus partidos."""

        estadios = ConsultaController.obtener_estadios()

        if not estadios:
            messagebox.showinfo("Sin datos", "No hay estadios registrados.")
            return

        # Ventana emergente para elegir estadio
        popup = tk.Toplevel(self.ventana)
        popup.title("Elegir estadio")
        popup.geometry("320x150")

        tk.Label(popup, text="Selecciona un estadio:").pack(pady=10)

        nombres = [f"{e[0]} - {e[1]}" for e in estadios]
        combo   = ttk.Combobox(popup, values=nombres, width=35, state="readonly")
        combo.pack(pady=5)
        combo.current(0)

        def buscar():
            seleccion  = combo.get()
            id_estadio = int(seleccion.split(" - ")[0])
            popup.destroy()

            datos = ConsultaController.partidos_por_estadio(id_estadio)

            if not datos:
                messagebox.showinfo("Sin resultados", "No hay partidos en ese estadio.")
                return

            self._mostrar(
                ("Fecha", "Estadio", "Local", "Visitante"),
                datos
            )

        tk.Button(popup, text="Buscar", command=buscar).pack(pady=10)

    # ── CONSULTA 3 ───────────────────────────────────────────
    def consulta_3(self):

        datos = ConsultaController.equipo_mas_costoso_por_pais_anfitrion()

        if not datos:
            messagebox.showinfo("Sin resultados", "No hay datos.")
            return

        self._mostrar(
            ("País anfitrión", "Equipo", "Valor total (€)"),
            datos
        )

    # ── CONSULTA 4 ───────────────────────────────────────────
    def consulta_4(self):

        datos = ConsultaController.jugadores_menores_21_por_equipo()

        if not datos:
            messagebox.showinfo("Sin resultados", "No hay jugadores menores de 21 años.")
            return

        self._mostrar(
            ("Equipo", "Jugadores < 21 años"),
            datos
        )