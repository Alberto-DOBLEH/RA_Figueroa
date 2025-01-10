import mysql.connector

def conexion_bd():
    mysql.connector.connect(host= 'localhost', user= 'root', password = 'root', database = 'airport')
