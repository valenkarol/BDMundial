from database.conexion import conectar
from datetime import datetime


class BitacoraController:

    @staticmethod
    def registrar_ingreso(id_usuario):

        conexion = conectar()

        cursor = conexion.cursor()

        ahora = datetime.now()

        fecha = ahora.date()

        hora = ahora.time()

        query = """
        INSERT INTO bitacora(
        accion,
        fecha_ingreso,
        hora_ingreso,
        id_usuario
        )
        VALUES(%s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (
                "INGRESO",
                fecha,
                hora,
                id_usuario
            )
        )

        conexion.commit()

        conexion.close()