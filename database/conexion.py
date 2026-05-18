import mariadb

def conectar():
    conexion = mariadb.connect(
        host="localhost",
        port=3307,
        user="root",
        password="12345",
        database="mundial2026"
    )

    return conexion