import tkinter as tk
from tkinter import ttk, messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

from database.conexion import conectar


# ════════════════════════════════════════════════════════════
# REPORTE 3
# Jugadores filtrados por peso, estatura y equipo
# ════════════════════════════════════════════════════════════

def _obtener_equipos():
    conexion = conectar()
    cursor   = conexion.cursor()
    cursor.execute("SELECT id_equipo, nombre FROM equipo ORDER BY nombre")
    datos = cursor.fetchall()
    conexion.close()
    return datos


def reporte_jugadores_por_filtro():
    """
    Reporte: jugadores cuyo peso, estatura y equipo
    están dentro de lo solicitado por el usuario.
    """

    equipos = _obtener_equipos()

    # ── Ventana de parámetros ────────────────────────────────
    popup = tk.Toplevel()
    popup.title("Parámetros — Reporte Jugadores")
    popup.geometry("360x300")

    tk.Label(popup, text="Peso mínimo (kg):").pack(pady=4)
    entrada_peso_min = tk.Entry(popup, width=20)
    entrada_peso_min.insert(0, "0")
    entrada_peso_min.pack()

    tk.Label(popup, text="Peso máximo (kg):").pack(pady=4)
    entrada_peso_max = tk.Entry(popup, width=20)
    entrada_peso_max.insert(0, "999")
    entrada_peso_max.pack()

    tk.Label(popup, text="Estatura mínima (m):").pack(pady=4)
    entrada_est_min = tk.Entry(popup, width=20)
    entrada_est_min.insert(0, "0")
    entrada_est_min.pack()

    tk.Label(popup, text="Estatura máxima (m):").pack(pady=4)
    entrada_est_max = tk.Entry(popup, width=20)
    entrada_est_max.insert(0, "9")
    entrada_est_max.pack()

    tk.Label(popup, text="Equipo:").pack(pady=4)
    nombres_eq = ["Todos"] + [f"{e[0]} - {e[1]}" for e in equipos]
    combo_eq   = ttk.Combobox(popup, values=nombres_eq, width=33, state="readonly")
    combo_eq.pack(pady=2)
    combo_eq.current(0)

    def generar():

        try:
            peso_min = float(entrada_peso_min.get())
            peso_max = float(entrada_peso_max.get())
            est_min  = float(entrada_est_min.get())
            est_max  = float(entrada_est_max.get())
        except ValueError:
            messagebox.showwarning("Error", "Ingresa valores numéricos válidos.")
            return

        seleccion_eq = combo_eq.get()
        popup.destroy()

        # ── Consulta ─────────────────────────────────────────
        conexion = conectar()
        cursor   = conexion.cursor()

        if seleccion_eq == "Todos":
            query = """
            SELECT
                j.nombre, j.posicion, j.peso, j.estatura, e.nombre
            FROM jugador j
            INNER JOIN equipo e ON j.id_equipo = e.id_equipo
            WHERE j.peso     BETWEEN %s AND %s
              AND j.estatura BETWEEN %s AND %s
            ORDER BY e.nombre, j.nombre
            """
            cursor.execute(query, (peso_min, peso_max, est_min, est_max))
            nombre_equipo = "Todos los equipos"
        else:
            id_equipo     = int(seleccion_eq.split(" - ")[0])
            nombre_equipo = seleccion_eq.split(" - ")[1]
            query = """
            SELECT
                j.nombre, j.posicion, j.peso, j.estatura, e.nombre
            FROM jugador j
            INNER JOIN equipo e ON j.id_equipo = e.id_equipo
            WHERE j.peso     BETWEEN %s AND %s
              AND j.estatura BETWEEN %s AND %s
              AND j.id_equipo = %s
            ORDER BY j.nombre
            """
            cursor.execute(query, (peso_min, peso_max, est_min, est_max, id_equipo))

        resultados = cursor.fetchall()
        conexion.close()

        # ── Generar PDF ───────────────────────────────────────
        ruta = "reporte_jugadores_filtro.pdf"
        pdf  = canvas.Canvas(ruta, pagesize=A4)
        ancho, alto = A4

        pdf.setFont("Helvetica-Bold", 15)
        pdf.drawCentredString(ancho / 2, alto - 50,
                              "REPORTE — JUGADORES POR FILTRO")

        pdf.setFont("Helvetica", 11)
        pdf.drawCentredString(
            ancho / 2, alto - 68,
            f"Peso: {peso_min}–{peso_max} kg  |  "
            f"Estatura: {est_min}–{est_max} m  |  "
            f"Equipo: {nombre_equipo}"
        )

        pdf.line(40, alto - 78, ancho - 40, alto - 78)

        y = alto - 96
        pdf.setFont("Helvetica-Bold", 10)
        pdf.drawString(40,  y, "Jugador")
        pdf.drawString(190, y, "Posición")
        pdf.drawString(290, y, "Peso")
        pdf.drawString(340, y, "Estatura")
        pdf.drawString(400, y, "Equipo")
        pdf.line(40, y - 5, ancho - 40, y - 5)
        y -= 20

        pdf.setFont("Helvetica", 10)

        if not resultados:
            pdf.drawString(40, y, "Sin jugadores con esos parámetros.")
        else:
            for r in resultados:
                if y < 60:
                    pdf.showPage()
                    y = alto - 60
                    pdf.setFont("Helvetica", 10)

                pdf.drawString(40,  y, str(r[0]))
                pdf.drawString(190, y, str(r[1]))
                pdf.drawString(290, y, f"{r[2]} kg")
                pdf.drawString(340, y, f"{r[3]} m")
                pdf.drawString(400, y, str(r[4]))
                y -= 18

        pdf.save()
        messagebox.showinfo("Listo", f"PDF generado: {os.path.abspath(ruta)}")

    tk.Button(popup, text="Generar PDF", command=generar).pack(pady=12)


# ════════════════════════════════════════════════════════════
# REPORTE 4
# Partidos por país anfitrión (México, USA, Canadá)
# ════════════════════════════════════════════════════════════

def reporte_partidos_por_pais_anfitrion():
    """
    Reporte: lista los partidos que se jugarán en cada
    país anfitrión (México, USA, Canadá).
    """

    # ── Consulta ─────────────────────────────────────────────
    conexion = conectar()
    cursor   = conexion.cursor()

    query = """
    SELECT
        pa.nombre           AS pais,
        ci.nombre           AS ciudad,
        es.nombre           AS estadio,
        p.fecha             AS fecha,
        local.nombre        AS equipo_local,
        visitante.nombre    AS equipo_visitante
    FROM partido p
    INNER JOIN estadio   es        ON p.id_estadio          = es.id_estadio
    INNER JOIN ciudad    ci        ON es.id_ciudad           = ci.id_ciudad
    INNER JOIN pais      pa        ON ci.pais_sede           = pa.id_pais
    INNER JOIN equipo    local     ON p.id_equipo_local      = local.id_equipo
    INNER JOIN equipo    visitante ON p.id_equipo_visitante  = visitante.id_equipo
    WHERE pa.nombre IN ('México', 'USA', 'Canadá')
    ORDER BY pa.nombre, p.fecha
    """

    cursor.execute(query)
    resultados = cursor.fetchall()
    conexion.close()

    # ── Generar PDF ───────────────────────────────────────────
    ruta = "reporte_partidos_pais_anfitrion.pdf"
    pdf  = canvas.Canvas(ruta, pagesize=A4)
    ancho, alto = A4

    pdf.setFont("Helvetica-Bold", 15)
    pdf.drawCentredString(ancho / 2, alto - 50,
                          "REPORTE — PARTIDOS POR PAÍS ANFITRIÓN")

    pdf.setFont("Helvetica", 11)
    pdf.drawCentredString(ancho / 2, alto - 68,
                          "México  |  USA  |  Canadá")

    pdf.line(40, alto - 78, ancho - 40, alto - 78)

    y = alto - 96
    pdf.setFont("Helvetica-Bold", 9)
    pdf.drawString(40,  y, "País")
    pdf.drawString(110, y, "Ciudad")
    pdf.drawString(200, y, "Estadio")
    pdf.drawString(310, y, "Fecha")
    pdf.drawString(375, y, "Local")
    pdf.drawString(470, y, "Visitante")
    pdf.line(40, y - 5, ancho - 40, y - 5)
    y -= 18

    pdf.setFont("Helvetica", 9)

    pais_actual = None

    if not resultados:
        pdf.drawString(40, y, "Sin partidos registrados.")
    else:
        for r in resultados:
            if y < 60:
                pdf.showPage()
                y = alto - 60
                pdf.setFont("Helvetica", 9)

            # Separador visual cuando cambia el país
            if r[0] != pais_actual:
                pais_actual = r[0]
                y -= 4
                pdf.setFont("Helvetica-Bold", 9)
                pdf.drawString(40, y, f"── {pais_actual} ──")
                pdf.setFont("Helvetica", 9)
                y -= 16

            pdf.drawString(40,  y, str(r[0]))
            pdf.drawString(110, y, str(r[1]))
            pdf.drawString(200, y, str(r[2]))
            pdf.drawString(310, y, str(r[3]))
            pdf.drawString(375, y, str(r[4]))
            pdf.drawString(470, y, str(r[5]))
            y -= 16

    pdf.save()
    messagebox.showinfo("Listo", f"PDF generado: {os.path.abspath(ruta)}")