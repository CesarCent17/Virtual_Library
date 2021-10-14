from dao.connection import *
from models.entidades import *

class Crud:

    #Objeto conexion
    def __init__(self):
        self.obj_conexion = Conexion()

    def createUsers(self, tupla):
        obj = None
        cnn = self.obj_conexion.conectar()
        cur = cnn.cursor()
        sql = f"INSERT INTO usuario (nombre, apellido, usuario, contrasena) " \
                f"VALUES(%s,%s ,%s,%s)"
        cur.execute(sql, tupla)
        cur.execute(f"SELECT * FROM usuario WHERE usuario = '{tupla[2]}' and contrasena = '{tupla[3]}'")
        datos = cur.fetchall()
        if len(datos) == 1:
            obj = Usuario(datos[0][0], datos[0][1], datos[0][2], datos[0][3])
        cnn.commit()
        cur.close()
        return obj

    def getAuth(self, usuario, password):
        obj = None
        cnn = self.obj_conexion.conectar()
        cur = cnn.cursor()
        cur.execute(f"SELECT * FROM usuario WHERE usuario = '{usuario}' and contrasena = '{password}'")
        datos = cur.fetchall()
        if len(datos) == 1:
            obj = Usuario(datos[0][0], datos[0][1], datos[0][2], datos[0][3])
        cur.close()
        return obj

    def updateUsers(self, tupla):
        obj = None
        cnn = self.obj_conexion.conectar()
        cur = cnn.cursor()
        sql = f"UPDATE usuario\
        SET nombre = %s, apellido = %s, usuario = %s, contrasena =\
        %s WHERE usuario = %s"
        cur.execute(sql, tupla)
        cur.execute(f"SELECT * FROM usuario WHERE usuario = '{tupla[2]}' and contrasena = '{tupla[3]}'")
        datos = cur.fetchall()
        if len(datos) == 1:
            obj = Usuario(datos[0][0], datos[0][1], datos[0][2], datos[0][3])
        cnn.commit()
        cur.close()
        return obj


    def getAuthSettings(self, nombre, apellido):
        obj = None
        cnn = self.obj_conexion.conectar()
        cur = cnn.cursor()
        cur.execute(f"SELECT * FROM usuario WHERE nombre = '{nombre}' and apellido = '{apellido}'")
        datos = cur.fetchall()
        if len(datos) == 1:
            obj = Usuario(datos[0][0], datos[0][1], datos[0][2], datos[0][3])
        cur.close()
        return obj

    def deleteUsers(self, usuario, contrasena):
        cnn = self.obj_conexion.conectar()
        cur = cnn.cursor()
        sql = f"DELETE FROM usuario WHERE usuario = '{usuario}' and contrasena = '{contrasena}'"
        cur.execute(sql)
        contar = cur.rowcount
        cnn.commit()
        cur.close()
        return contar


