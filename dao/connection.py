import mysql.connector

class Conexion:
    def conectar(self):
        dic = {"host" : "localhost", "user" :"root",
            "passwd" :"Artn0w21", "database" :"biblioteca"}
        conectarDB = None
        try:
            conectarDB= mysql.connector.connect(**dic)

        except(mysql.connector.DatabaseError, mysql.connector.OperationalError, mysql.connector.IntegrityError) as e:
            print("Error de conexion"+ str(e))
        return conectarDB




