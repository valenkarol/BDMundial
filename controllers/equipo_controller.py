from database.conexion import conectar


class EquipoController:

    @staticmethod
    def insertar_equipo(
        nombre,
        id_confederacion,
        id_grupo,
        id_director,
        id_pais
    ):

        conexion = conectar()

        cursor = conexion.cursor()

        query = """
        INSERT INTO equipo(
        nombre,
        id_confederacion,
        id_grupo,
        id_director,
        id_pais
        )
        VALUES(%s,%s,%s,%s,%s)
        """

        cursor.execute(
            query,
            (
                nombre,
                id_confederacion,
                id_grupo,
                id_director,
                id_pais
            )
        )

        conexion.commit()

        conexion.close()
        
        
    @staticmethod
    def eliminar_equipo(id_equipo):
        conexion = conectar()
        
        cursor = conexion.cursor()
        
        query = """
        DELETE FROM equipo
        WHERE id_equipo = %s
        """
        
        cursor.execute(query, (id_equipo,))
        
        conexion.commit()
        
        conexion.close()

    @staticmethod
    def obtener_equipos():

        conexion = conectar()

        cursor = conexion.cursor()

        query = """
        SELECT
        e.id_equipo,
        e.nombre,
        c.nombre,
        g.nombre,
        d.nombre,
        p.nombre
        FROM equipo e
        INNER JOIN confederacion c
        ON e.id_confederacion = c.id_confederacion
        INNER JOIN grupo g
        ON e.id_grupo = g.id_grupo
        INNER JOIN director_tecnico d
        ON e.id_director = d.id_director
        INNER JOIN pais p
        ON e.id_pais = p.id_pais
        """

        cursor.execute(query)

        resultados = cursor.fetchall()

        conexion.close()

        return resultados