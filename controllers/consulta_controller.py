from database.conexion import conectar


class ConsultaController:

    # ─────────────────────────────────────────────────────────
    # CONSULTA 1
    # Jugador más costoso por confederación
    # ─────────────────────────────────────────────────────────
    @staticmethod
    def jugador_mas_costoso_por_confederacion():

        conexion = conectar()
        cursor   = conexion.cursor()

        query = """
        SELECT
            c.nombre  AS confederacion,
            j.nombre  AS jugador,
            j.valor   AS valor
        FROM jugador j
        INNER JOIN equipo       e  ON j.id_equipo        = e.id_equipo
        INNER JOIN confederacion c  ON e.id_confederacion = c.id_confederacion
        WHERE j.valor = (
            SELECT MAX(j2.valor)
            FROM jugador j2
            INNER JOIN equipo e2 ON j2.id_equipo = e2.id_equipo
            WHERE e2.id_confederacion = c.id_confederacion
        )
        ORDER BY c.nombre
        """

        cursor.execute(query)
        resultados = cursor.fetchall()
        conexion.close()
        return resultados

    # ─────────────────────────────────────────────────────────
    # CONSULTA 2
    # Partidos que se jugarán en un estadio elegido por el usuario
    # ─────────────────────────────────────────────────────────
    @staticmethod
    def partidos_por_estadio(id_estadio):

        conexion = conectar()
        cursor   = conexion.cursor()

        query = """
        SELECT
            p.fecha            AS fecha,
            es.nombre          AS estadio,
            local.nombre       AS equipo_local,
            visitante.nombre   AS equipo_visitante
        FROM partido p
        INNER JOIN estadio es        ON p.id_estadio          = es.id_estadio
        INNER JOIN equipo  local     ON p.id_equipo_local      = local.id_equipo
        INNER JOIN equipo  visitante ON p.id_equipo_visitante  = visitante.id_equipo
        WHERE es.id_estadio = %s
        ORDER BY p.fecha
        """

        cursor.execute(query, (id_estadio,))
        resultados = cursor.fetchall()
        conexion.close()
        return resultados

    # ─────────────────────────────────────────────────────────
    # CONSULTA 3
    # Equipo más costoso por país anfitrión (México, USA, Canadá)
    # ─────────────────────────────────────────────────────────
    @staticmethod
    def equipo_mas_costoso_por_pais_anfitrion():

        conexion = conectar()
        cursor   = conexion.cursor()

        query = """
        SELECT
            pa_sede.nombre   AS pais_anfitrion,
            eq.nombre        AS equipo,
            SUM(j.valor)     AS valor_total
        FROM partido p
        INNER JOIN estadio  es       ON p.id_estadio         = es.id_estadio
        INNER JOIN ciudad   ci       ON es.id_ciudad          = ci.id_ciudad
        INNER JOIN pais     pa_sede  ON ci.pais_sede          = pa_sede.id_pais
        INNER JOIN equipo   eq       ON p.id_equipo_local     = eq.id_equipo
        INNER JOIN jugador  j        ON j.id_equipo           = eq.id_equipo
        WHERE pa_sede.nombre IN ('México', 'USA', 'Canadá')
        GROUP BY pa_sede.nombre, eq.nombre
        HAVING SUM(j.valor) = (
            SELECT MAX(sub_total)
            FROM (
                SELECT SUM(j2.valor) AS sub_total
                FROM partido        p2
                INNER JOIN estadio  es2 ON p2.id_estadio     = es2.id_estadio
                INNER JOIN ciudad   ci2 ON es2.id_ciudad      = ci2.id_ciudad
                INNER JOIN pais     pa2 ON ci2.pais_sede      = pa2.id_pais
                INNER JOIN equipo   eq2 ON p2.id_equipo_local = eq2.id_equipo
                INNER JOIN jugador  j2  ON j2.id_equipo       = eq2.id_equipo
                WHERE pa2.nombre = pa_sede.nombre
                GROUP BY eq2.id_equipo
            ) AS totales
        )
        ORDER BY pa_sede.nombre
        """

        cursor.execute(query)
        resultados = cursor.fetchall()
        conexion.close()
        return resultados

    # ─────────────────────────────────────────────────────────
    # CONSULTA 4
    # Cantidad de jugadores menores de 21 años por equipo
    # ─────────────────────────────────────────────────────────
    @staticmethod
    def jugadores_menores_21_por_equipo():

        conexion = conectar()
        cursor   = conexion.cursor()

        query = """
        SELECT
            e.nombre          AS equipo,
            COUNT(j.id_jugador) AS cantidad
        FROM jugador j
        INNER JOIN equipo e ON j.id_equipo = e.id_equipo
        WHERE j.edad < 21
        GROUP BY e.nombre
        ORDER BY cantidad DESC
        """

        cursor.execute(query)
        resultados = cursor.fetchall()
        conexion.close()
        return resultados

    # ─────────────────────────────────────────────────────────
    # AUXILIAR — lista de estadios para el combobox
    # ─────────────────────────────────────────────────────────
    @staticmethod
    def obtener_estadios():

        conexion = conectar()
        cursor   = conexion.cursor()
        cursor.execute("SELECT id_estadio, nombre FROM estadio ORDER BY nombre")
        resultados = cursor.fetchall()
        conexion.close()
        return resultados