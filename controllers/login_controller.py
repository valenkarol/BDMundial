from database.conexion import conectar


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

        return resultado