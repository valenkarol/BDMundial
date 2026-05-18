class Bitacora:

    def __init__(
        self,
        accion,
        fecha_ingreso,
        fecha_salida,
        hora_ingreso,
        hora_salida,
        id_usuario
    ):

        self.accion = accion
        self.fecha_ingreso = fecha_ingreso
        self.fecha_salida = fecha_salida
        self.hora_ingreso = hora_ingreso
        self.hora_salida = hora_salida
        self.id_usuario = id_usuario