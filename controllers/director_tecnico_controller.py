from database.conexion import conectar


class DirectorTecnicoController:

    @staticmethod
    def insertar_director(nombre):

        conexion = conectar()

        cursor = conexion.cursor()

        query = """
        INSERT INTO director_tecnico(nombre)
        VALUES(%s)
        """

        cursor.execute(query, (nombre,))

        conexion.commit()

        conexion.close()

    @staticmethod
    def obtener_directores():

        conexion = conectar()

        cursor = conexion.cursor()

        query = """
        SELECT *
        FROM director_tecnico
        """

        cursor.execute(query)

        resultados = cursor.fetchall()

        conexion.close()

        return resultados