import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from tkcalendar import DateEntry

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

import os

from database.conexion import conectar


def generar_reporte_usuarios():

    # ─────────────────────────────
    # VENTANA
    # ─────────────────────────────

    popup = tk.Toplevel()

    popup.title("Reporte Usuarios")

    popup.geometry("350x300")

    # ─────────────────────────────
    # FECHA
    # ─────────────────────────────

    tk.Label(
        popup,
        text="Fecha"
    ).pack(pady=5)

    entrada_fecha = DateEntry(
        popup,
        width=25,
        background="darkblue",
        foreground="white",
        borderwidth=2,
        date_pattern="yyyy-mm-dd"
    )

    entrada_fecha.pack()

    # ─────────────────────────────
    # HORA INICIO
    # ─────────────────────────────

    tk.Label(
        popup,
        text="Hora inicio"
    ).pack(pady=5)

    horas = []

    for h in range(24):

        for m in range(0, 60, 5):

            horas.append(
                f"{h:02}:{m:02}"
            )

    combo_inicio = ttk.Combobox(
        popup,
        values=horas,
        state="readonly",
        width=22
    )

    combo_inicio.pack()

    # ─────────────────────────────
    # HORA FIN
    # ─────────────────────────────

    tk.Label(
        popup,
        text="Hora fin"
    ).pack(pady=5)

    combo_fin = ttk.Combobox(
        popup,
        values=horas,
        state="readonly",
        width=22
    )

    combo_fin.pack()

    # ─────────────────────────────
    # GENERAR PDF
    # ─────────────────────────────

    def generar():

        fecha = entrada_fecha.get()

        hora_ini = combo_inicio.get()

        hora_fin = combo_fin.get()

        if (
            hora_ini == ""
            or hora_fin == ""
        ):

            messagebox.showerror(
                "Error",
                "Seleccione las horas"
            )

            return

        # ─────────────────────────────
        # CONSULTA SQL
        # ─────────────────────────────

        conexion = conectar()

        cursor = conexion.cursor()

        query = """
        SELECT
            u.nombreUsuario,
            u.rol,
            b.fecha_ingreso,
            b.hora_ingreso,
            b.fecha_salida,
            b.hora_salida
        FROM bitacora b
        INNER JOIN usuario u
        ON b.id_usuario = u.id_usuario
        WHERE b.fecha_ingreso = %s
        AND b.hora_ingreso >= %s
        AND b.hora_ingreso <= %s
        ORDER BY b.hora_ingreso
        """

        cursor.execute(
            query,
            (
                fecha,
                hora_ini,
                hora_fin
            )
        )

        resultados = cursor.fetchall()

        conexion.close()

        # ─────────────────────────────
        # PDF
        # ─────────────────────────────

        ruta = "reporte_usuarios.pdf"

        pdf = canvas.Canvas(
            ruta,
            pagesize=A4
        )

        ancho, alto = A4

        # TÍTULO

        pdf.setFont(
            "Helvetica-Bold",
            16
        )

        pdf.drawCentredString(
            ancho / 2,
            alto - 50,
            "REPORTE DE USUARIOS"
        )

        pdf.setFont(
            "Helvetica",
            11
        )

        pdf.drawCentredString(
            ancho / 2,
            alto - 70,
            f"Fecha: {fecha}"
        )

        pdf.drawCentredString(
            ancho / 2,
            alto - 85,
            f"Horario: {hora_ini} - {hora_fin}"
        )

        # LÍNEA

        pdf.line(
            40,
            alto - 100,
            ancho - 40,
            alto - 100
        )

        # ENCABEZADOS

        y = alto - 125

        pdf.setFont(
            "Helvetica-Bold",
            10
        )

        pdf.drawString(40, y, "Usuario")
        pdf.drawString(150, y, "Rol")
        pdf.drawString(250, y, "Ingreso")
        pdf.drawString(400, y, "Salida")

        y -= 20

        pdf.setFont(
            "Helvetica",
            10
        )

        # DATOS

        if not resultados:

            pdf.drawString(
                40,
                y,
                "No hay registros."
            )

        else:

            for r in resultados:

                if y < 60:

                    pdf.showPage()

                    y = alto - 60

                ingreso = (
                    f"{r[2]} {str(r[3])[:5]}"
                )

                salida = "—"

                if r[4] and r[5]:

                    salida = (
                        f"{r[4]} {str(r[5])[:5]}"
                    )

                pdf.drawString(
                    40,
                    y,
                    str(r[0])
                )

                pdf.drawString(
                    150,
                    y,
                    str(r[1])
                )

                pdf.drawString(
                    250,
                    y,
                    ingreso
                )

                pdf.drawString(
                    400,
                    y,
                    salida
                )

                y -= 18

        pdf.save()

        messagebox.showinfo(
            "Correcto",
            f"PDF generado:\n{os.path.abspath(ruta)}"
        )

        popup.destroy()

    # ─────────────────────────────
    # BOTÓN
    # ─────────────────────────────

    tk.Button(
        popup,
        text="Generar PDF",
        width=20,
        height=2,
        command=generar
    ).pack(pady=20)