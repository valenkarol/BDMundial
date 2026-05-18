from database.conexion import conectar


class PartidoController:

    @staticmethod
    def insertar_partido(
        fecha,
        id_estadio,
        id_equipo_local
    ):

        conexion = conectar()

        cursor = conexion.cursor()

        query = """
        INSERT INTO partido(
        fecha,
        id_estadio,
        id_equipo_local
        )
        VALUES(%s, %s, %s)
        """

        cursor.execute(
            query,
            (
                fecha,
                id_estadio,
                id_equipo_local
            )
        )

        conexion.commit()

        conexion.close()

    @staticmethod
    def obtener_partidos():

        conexion = conectar()

        cursor = conexion.cursor()

        query = """
        SELECT p.id_partido,
               p.fecha,
               e.nombre,
               eq.nombre
        FROM partido p
        INNER JOIN estadio e
        ON p.id_estadio = e.id_estadio
        INNER JOIN equipo eq
        ON p.id_equipo_local = eq.id_equipo
        """

        cursor.execute(query)

        resultados = cursor.fetchall()

        conexion.close()

        return resultados