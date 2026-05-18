from database.conexion import conectar
from views.login import Login

Login()
try:
    conexion = conectar()
    print("Conexión exitosa")
except Exception as e:
    print("Error:", e)