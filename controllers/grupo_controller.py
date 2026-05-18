from database.conexion import conectar


class GrupoController:

    @staticmethod
    def obtener_grupos():

        conexion = conectar()

        cursor = conexion.cursor()

        query = "SELECT * FROM grupo"

        cursor.execute(query)

        resultados = cursor.fetchall()

        conexion.close()

        return resultados