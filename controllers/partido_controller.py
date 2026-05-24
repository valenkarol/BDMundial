from database.conexion import conectar


class PartidoController:

    @staticmethod
    def insertar_partido(
        fecha,
        id_estadio,
        id_local,
        id_visitante
    ):

        conexion = conectar()

        cursor = conexion.cursor()

        query = """
        INSERT INTO partido(
        fecha,
        id_estadio,
        id_equipo_local,
        id_equipo_visitante
        )
        VALUES(%s,%s,%s,%s)
        """

        cursor.execute(
            query,
            (
                fecha,
                id_estadio,
                id_local,
                id_visitante
            )
        )

        conexion.commit()

        conexion.close()
        
    @staticmethod
    def eliminar_partido(id_partido):
        
        conexion = conectar()
        cursor = conexion.cursor()
        
        query = """
        DELETE FROM partido
        WHERE id_partido = %s
        """
        
        cursor.execute(query, (id_partido,))
        
        conexion.commit()
        
        conexion.close()

    @staticmethod
    def obtener_partidos():

        conexion = conectar()

        cursor = conexion.cursor()

        query = """
        SELECT
        p.id_partido,
        p.fecha,
        es.nombre,
        el.nombre,
        ev.nombre
        FROM partido p
        INNER JOIN estadio es
        ON p.id_estadio = es.id_estadio
        INNER JOIN equipo el
        ON p.id_equipo_local = el.id_equipo
        INNER JOIN equipo ev
        ON p.id_equipo_visitante = ev.id_equipo
        """

        cursor.execute(query)

        resultados = cursor.fetchall()

        conexion.close()

        return resultados