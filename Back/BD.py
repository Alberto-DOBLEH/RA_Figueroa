import mysql.connector

def conexion_bd():
    return mysql.connector.connect(host= 'localhost', user= 'root', password = 'root', database = 'airport')
