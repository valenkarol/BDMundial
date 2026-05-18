from database.conexion import conectar


class UsuarioController:

    @staticmethod
    def insertar_usuario(
        nombreUsuario,
        contrasena,
        rol
    ):

        conexion = conectar()

        cursor = conexion.cursor()

        query = """
        INSERT INTO usuario(
        nombreUsuario,
        contrasena,
        rol
        )
        VALUES(%s, %s, %s)
        """

        cursor.execute(
            query,
            (
                nombreUsuario,
                contrasena,
                rol
            )
        )

        conexion.commit()

        conexion.close()

    @staticmethod
    def obtener_usuarios():

        conexion = conectar()

        cursor = conexion.cursor()

        query = """
        SELECT *
        FROM usuario
        """

        cursor.execute(query)

        resultados = cursor.fetchall()

        conexion.close()

        return resultados