from database.conexion import conectar
from datetime import datetime


class BitacoraController:

    @staticmethod
    def registrar_ingreso(id_usuario):

        conexion = conectar()
        cursor = conexion.cursor()
        ahora = datetime.now()

        query = """
        INSERT INTO bitacora(
            accion,
            fecha_ingreso,
            hora_ingreso,
            id_usuario
        )
        VALUES(%s, %s, %s, %s)
        """

        cursor.execute(query, (
            "INGRESO",
            ahora.date(),
            ahora.time(),
            id_usuario
        ))

        conexion.commit()
        conexion.close()

    @staticmethod
    def registrar_salida(id_usuario):
        """
        Actualiza el registro MÁS RECIENTE del usuario
        que aún no tiene hora de salida.
        """
        conexion = conectar()
        cursor = conexion.cursor()
        ahora = datetime.now()

        query = """
        UPDATE bitacora
        SET
            accion       = 'SALIDA',
            fecha_salida = %s,
            hora_salida  = %s
        WHERE id_usuario  = %s
          AND fecha_salida IS NULL
          AND hora_salida  IS NULL
        ORDER BY id_bitacora DESC
        LIMIT 1
        """

        cursor.execute(query, (
            ahora.date(),
            ahora.time(),
            id_usuario
        ))

        conexion.commit()
        conexion.close()