from reportlab.pdfgen import canvas

from controllers.usuario_controller import UsuarioController


def generar_reporte_usuarios():

    usuarios = UsuarioController.obtener_usuarios()

    pdf = canvas.Canvas(
        "reporte_usuarios.pdf"
    )

    pdf.setFont("Helvetica", 14)

    pdf.drawString(
        200,
        800,
        "REPORTE USUARIOS"
    )

    y = 750

    for usuario in usuarios:

        texto = f"""
        ID: {usuario[0]}
        Usuario: {usuario[1]}
        Rol: {usuario[3]}
        """

        pdf.drawString(50, y, texto)

        y -= 30

    pdf.save()

    print("Reporte generado")