from database.conexion import conectar


class EquipoController:

    @staticmethod
    def insertar_equipo(
        nombre,
        id_confederacion,
        id_grupo,
        id_director
    ):

        conexion = conectar()

        cursor = conexion.cursor()

        query = """
        INSERT INTO equipo(
        nombre,
        id_confederacion,
        id_grupo,
        id_director
        )
        VALUES(%s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (
                nombre,
                id_confederacion,
                id_grupo,
                id_director
            )
        )

        conexion.commit()

        conexion.close()

    @staticmethod
    def obtener_equipos():

        conexion = conectar()

        cursor = conexion.cursor()

        query = """
        SELECT e.id_equipo,
               e.nombre,
               c.nombre,
               g.nombre,
               d.nombre
        FROM equipo e
        INNER JOIN confederacion c
        ON e.id_confederacion = c.id_confederacion
        INNER JOIN grupo g
        ON e.id_grupo = g.id_grupo
        INNER JOIN director_tecnico d
        ON e.id_director = d.id_director
        """

        cursor.execute(query)

        resultados = cursor.fetchall()

        conexion.close()

        return resultados