from database.conexion import conectar


class ConfederacionController:

    @staticmethod
    def insertar_confederacion(nombre):

        conexion = conectar()

        cursor = conexion.cursor()

        query = """
        INSERT INTO confederacion(nombre)
        VALUES(%s)
        """

        cursor.execute(query, (nombre,))

        conexion.commit()

        conexion.close()

    @staticmethod
    def obtener_confederaciones():

        conexion = conectar()

        cursor = conexion.cursor()

        query = "SELECT * FROM confederacion"

        cursor.execute(query)

        resultados = cursor.fetchall()

        conexion.close()

        return resultados