import tkinter as tk
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

from database.conexion import conectar


def generar_reporte_usuarios():
    """
    Abre una ventana para que el usuario ingrese fecha y hora,
    luego genera el PDF con los registros de la bitácora que coincidan.
    """

    # ── Ventana de parámetros ────────────────────────────────
    popup = tk.Toplevel()
    popup.title("Parámetros — Reporte Usuarios")
    popup.geometry("340x220")

    tk.Label(popup, text="Fecha (YYYY-MM-DD):").pack(pady=5)
    entrada_fecha = tk.Entry(popup, width=25)
    entrada_fecha.pack()

    tk.Label(popup, text="Hora inicio (HH:MM):").pack(pady=5)
    entrada_hora_ini = tk.Entry(popup, width=25)
    entrada_hora_ini.pack()

    tk.Label(popup, text="Hora fin (HH:MM):").pack(pady=5)
    entrada_hora_fin = tk.Entry(popup, width=25)
    entrada_hora_fin.pack()

    def generar():

        fecha    = entrada_fecha.get().strip()
        hora_ini = entrada_hora_ini.get().strip()
        hora_fin = entrada_hora_fin.get().strip()

        if not fecha or not hora_ini or not hora_fin:
            messagebox.showwarning("Atención", "Completa todos los campos.")
            return

        popup.destroy()

        # ── Consulta ─────────────────────────────────────────
        conexion = conectar()
        cursor   = conexion.cursor()

        query = """
        SELECT
            u.nombreUsuario,
            u.rol,
            b.fecha_ingreso,
            b.hora_ingreso,
            b.fecha_salida,
            b.hora_salida
        FROM bitacora b
        INNER JOIN usuario u ON b.id_usuario = u.id_usuario
        WHERE b.fecha_ingreso = %s
          AND b.hora_ingreso  >= %s
          AND b.hora_ingreso  <= %s
        ORDER BY b.hora_ingreso
        """

        cursor.execute(query, (fecha, hora_ini, hora_fin))
        resultados = cursor.fetchall()
        conexion.close()

        # ── Generar PDF ───────────────────────────────────────
        ruta = "reporte_usuarios.pdf"
        pdf  = canvas.Canvas(ruta, pagesize=A4)
        ancho, alto = A4

        # Encabezado
        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawCentredString(ancho / 2, alto - 50,
                              "REPORTE DE USUARIOS — BITÁCORA")

        pdf.setFont("Helvetica", 11)
        pdf.drawCentredString(ancho / 2, alto - 70,
                              f"Fecha: {fecha}   Rango: {hora_ini} — {hora_fin}")

        # Línea separadora
        pdf.line(40, alto - 80, ancho - 40, alto - 80)

        # Encabezados de columna
        y = alto - 100
        pdf.setFont("Helvetica-Bold", 10)
        pdf.drawString(40,  y, "Usuario")
        pdf.drawString(160, y, "Rol")
        pdf.drawString(250, y, "Ingreso")
        pdf.drawString(370, y, "Salida")

        pdf.line(40, y - 5, ancho - 40, y - 5)
        y -= 20

        # Filas
        pdf.setFont("Helvetica", 10)

        if not resultados:
            pdf.drawString(40, y, "Sin registros para ese rango.")
        else:
            for r in resultados:
                if y < 60:               # salto de página
                    pdf.showPage()
                    y = alto - 60
                    pdf.setFont("Helvetica", 10)

                ingreso = f"{r[2]} {str(r[3])[:5]}" if r[2] else "—"
                salida  = f"{r[4]} {str(r[5])[:5]}" if r[4] else "—"

                pdf.drawString(40,  y, str(r[0]))
                pdf.drawString(160, y, str(r[1]))
                pdf.drawString(250, y, ingreso)
                pdf.drawString(370, y, salida)
                y -= 18

        pdf.save()
        messagebox.showinfo("Listo", f"PDF generado: {os.path.abspath(ruta)}")

    tk.Button(popup, text="Generar PDF", command=generar).pack(pady=15)