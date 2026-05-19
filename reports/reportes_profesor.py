from reportlab.pdfgen import canvas

from database.conexion import conectar


def reporte_valor_equipos():

    conexion = conectar()

    cursor = conexion.cursor()

    query = """
    SELECT
    c.nombre,
    e.nombre,
    SUM(j.valor)
    FROM jugador j
    INNER JOIN equipo e
    ON j.id_equipo = e.id_equipo
    INNER JOIN confederacion c
    ON e.id_confederacion = c.id_confederacion
    GROUP BY e.nombre
    """

    cursor.execute(query)

    resultados = cursor.fetchall()

    pdf = canvas.Canvas(
        "reporte_valor_equipos.pdf"
    )

    y = 800

    pdf.drawString(
        200,
        y,
        "REPORTE VALOR EQUIPOS"
    )

    y -= 50

    for r in resultados:

        texto = f"""
        Confederacion: {r[0]}
        Equipo: {r[1]}
        Valor: {r[2]}
        """

        pdf.drawString(50, y, texto)

        y -= 30

    pdf.save()

    conexion.close()