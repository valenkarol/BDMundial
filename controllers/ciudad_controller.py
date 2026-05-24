from database.conexion import conectar


class CiudadController:

    @staticmethod
    def insertar_ciudad(nombre, pais_sede):

        conexion = conectar()

        cursor = conexion.cursor()

        query = """
        INSERT INTO ciudad(nombre, pais_sede)
        VALUES(%s, %s)
        """

        cursor.execute(query, (nombre, pais_sede))

        conexion.commit()

        conexion.close()
        
    @staticmethod
    def eliminar_ciudad(id_ciudad):
        conexion = conectar()
        cursor = conexion.cursor()
        
        query = """
        DELETE FROM ciudad
        WHERE id_ciudad = %s
        """
        
        cursor.execute(query, (id_ciudad,))
        
        conexion.commit()
        
        conexion.close()

    @staticmethod
    def obtener_ciudades():

        conexion = conectar()

        cursor = conexion.cursor()

        query = """
        SELECT c.id_ciudad,
               c.nombre,
               p.nombre
        FROM ciudad c
        INNER JOIN pais p
        ON c.pais_sede = p.id_pais
        """

        cursor.execute(query)

        resultados = cursor.fetchall()

        conexion.close()

        return resultados