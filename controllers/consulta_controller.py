from database.conexion import conectar


class ConsultaController:

    @staticmethod
    def partidos_por_estadio(id_estadio):

        conexion = conectar()

        cursor = conexion.cursor()

        query = """
        SELECT
        p.fecha,
        e.nombre,
        eq.nombre
        FROM partido p
        INNER JOIN estadio e
        ON p.id_estadio = e.id_estadio
        INNER JOIN equipo eq
        ON p.id_equipo_local = eq.id_equipo
        WHERE e.id_estadio = %s
        """

        cursor.execute(query, (id_estadio,))

        resultados = cursor.fetchall()

        conexion.close()

        return resultados