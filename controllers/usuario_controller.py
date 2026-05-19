from database.conexion import conectar


class UsuarioController:

    @staticmethod
    def insertar_usuario(
        usuario,
        password,
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
                usuario,
                password,
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