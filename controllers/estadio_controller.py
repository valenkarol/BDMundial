from database.conexion import conectar


class EstadioController:

    @staticmethod
    def insertar_estadio(nombre, capacidad, id_ciudad):

        conexion = conectar()

        cursor = conexion.cursor()

        query = """
        INSERT INTO estadio(
        nombre,
        capacidad,
        id_ciudad
        )
        VALUES(%s, %s, %s)
        """

        cursor.execute(
            query,
            (nombre, capacidad, id_ciudad)
        )

        conexion.commit()

        conexion.close()

    @staticmethod
    def obtener_estadios():

        conexion = conectar()

        cursor = conexion.cursor()

        query = """
        SELECT e.id_estadio,
               e.nombre,
               e.capacidad,
               c.nombre
        FROM estadio e
        INNER JOIN ciudad c
        ON e.id_ciudad = c.id_ciudad
        """

        cursor.execute(query)

        resultados = cursor.fetchall()

        conexion.close()

        return resultados