from database.conexion import conectar


class JugadorController:

    @staticmethod
    def insertar_jugador(
        nombre,
        posicion,
        numero,
        valor,
        edad,
        peso,
        estatura,
        id_equipo
    ):

        conexion = conectar()

        cursor = conexion.cursor()

        query = """
        INSERT INTO jugador(
        nombre,
        posicion,
        numero,
        valor,
        edad,
        peso,
        estatura,
        id_equipo
        )
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
        """

        cursor.execute(
            query,
            (
                nombre,
                posicion,
                numero,
                valor,
                edad,
                peso,
                estatura,
                id_equipo
            )
        )

        conexion.commit()

        conexion.close()

    @staticmethod
    def obtener_jugadores():

        conexion = conectar()

        cursor = conexion.cursor()

        query = """
        SELECT j.id_jugador,
               j.nombre,
               j.posicion,
               j.numero,
               j.valor,
               e.nombre
        FROM jugador j
        INNER JOIN equipo e
        ON j.id_equipo = e.id_equipo
        """

        cursor.execute(query)

        resultados = cursor.fetchall()

        conexion.close()

        return resultados