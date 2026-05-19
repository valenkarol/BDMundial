import tkinter as tk
from tkinter import ttk, messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

from database.conexion import conectar


def _obtener_confederaciones():
    conexion = conectar()
    cursor   = conexion.cursor()
    cursor.execute("SELECT id_confederacion, nombre FROM confederacion ORDER BY nombre")
    datos = cursor.fetchall()
    conexion.close()
    return datos


def reporte_valor_equipos():
    """
    Reporte: valor total de jugadores por equipo,
    filtrado por una confederación específica.
    """

    confederaciones = _obtener_confederaciones()

    if not confederaciones:
        messagebox.showwarning("Sin datos", "No hay confederaciones registradas.")
        return

    # ── Ventana de parámetros ────────────────────────────────
    popup = tk.Toplevel()
    popup.title("Parámetros — Reporte Valor Equipos")
    popup.geometry("340x160")

    tk.Label(popup, text="Selecciona la confederación:").pack(pady=10)

    nombres = [f"{c[0]} - {c[1]}" for c in confederaciones]
    combo   = ttk.Combobox(popup, values=nombres, width=35, state="readonly")
    combo.pack(pady=5)
    combo.current(0)

    def generar():

        seleccion        = combo.get()
        id_confederacion = int(seleccion.split(" - ")[0])
        nombre_conf      = seleccion.split(" - ")[1]
        popup.destroy()

        # ── Consulta ─────────────────────────────────────────
        conexion = conectar()
        cursor   = conexion.cursor()

        query = """
        SELECT
            e.nombre        AS equipo,
            COUNT(j.id_jugador) AS num_jugadores,
            SUM(j.valor)    AS valor_total
        FROM jugador j
        INNER JOIN equipo        e ON j.id_equipo        = e.id_equipo
        INNER JOIN confederacion c ON e.id_confederacion = c.id_confederacion
        WHERE c.id_confederacion = %s
        GROUP BY e.nombre
        ORDER BY valor_total DESC
        """

        cursor.execute(query, (id_confederacion,))
        resultados = cursor.fetchall()
        conexion.close()

        # ── Generar PDF ───────────────────────────────────────
        ruta = "reporte_valor_equipos.pdf"
        pdf  = canvas.Canvas(ruta, pagesize=A4)
        ancho, alto = A4

        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawCentredString(ancho / 2, alto - 50,
                              "REPORTE — VALOR TOTAL DE JUGADORES POR EQUIPO")

        pdf.setFont("Helvetica", 12)
        pdf.drawCentredString(ancho / 2, alto - 72,
                              f"Confederación: {nombre_conf}")

        pdf.line(40, alto - 82, ancho - 40, alto - 82)

        y = alto - 100
        pdf.setFont("Helvetica-Bold", 10)
        pdf.drawString(40,  y, "Equipo")
        pdf.drawString(230, y, "# Jugadores")
        pdf.drawString(360, y, "Valor total (€)")
        pdf.line(40, y - 5, ancho - 40, y - 5)
        y -= 20

        pdf.setFont("Helvetica", 10)

        if not resultados:
            pdf.drawString(40, y, "Sin resultados para esa confederación.")
        else:
            for r in resultados:
                if y < 60:
                    pdf.showPage()
                    y = alto - 60
                    pdf.setFont("Helvetica", 10)

                pdf.drawString(40,  y, str(r[0]))
                pdf.drawString(230, y, str(r[1]))
                pdf.drawString(360, y, f"€ {float(r[2]):,.2f}")
                y -= 18

        pdf.save()
        messagebox.showinfo("Listo", f"PDF generado: {os.path.abspath(ruta)}")

    tk.Button(popup, text="Generar PDF", command=generar).pack(pady=15)