from database.conexion import conectar

try:
    conexion = conectar()
    print("Conexión exitosa")
except Exception as e:
    print("Error:", e)