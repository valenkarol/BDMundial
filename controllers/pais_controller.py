from database.conexion import conectar


class PaisController:

    @staticmethod
    def insertar_pais(nombre):

        conexion = conectar()

        cursor = conexion.cursor()

        query = """
        INSERT INTO pais(nombre)
        VALUES(%s)
        """

        cursor.execute(query, (nombre,))

        conexion.commit()

        conexion.close()

    @staticmethod
    def obtener_paises():

        conexion = conectar()

        cursor = conexion.cursor()

        query = """
        SELECT *
        FROM pais
        """

        cursor.execute(query)

        resultados = cursor.fetchall()

        conexion.close()

        return resultados

    @staticmethod
    def eliminar_pais(id_pais):

        conexion = conectar()

        cursor = conexion.cursor()

        query = """
        DELETE FROM pais
        WHERE id_pais = %s
        """

        cursor.execute(query, (id_pais,))

        conexion.commit()

        conexion.close()

    @staticmethod
    def actualizar_pais(id_pais, nombre):

        conexion = conectar()

        cursor = conexion.cursor()

        query = """
        UPDATE pais
        SET nombre = %s
        WHERE id_pais = %s
        """

        cursor.execute(query, (nombre, id_pais))

        conexion.commit()

        conexion.close()