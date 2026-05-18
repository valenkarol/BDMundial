from database.conexion import conectar
from controllers.bitacora_controller import BitacoraController


class LoginController:

    @staticmethod
    def validar_usuario(usuario, password):

        conexion = conectar()

        cursor = conexion.cursor()

        query = """
        SELECT *
        FROM usuario
        WHERE nombreUsuario = %s
        AND contrasena = %s
        """

        cursor.execute(query, (usuario, password))

        resultado = cursor.fetchone()

        conexion.close()

        if resultado:

            BitacoraController.registrar_ingreso(
                resultado[0]
            )

        return resultado