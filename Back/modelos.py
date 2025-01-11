from BD import conexion_bd

#Se usa para obtener las reservaciones por usuario por medio de su id
def obtener_reservaciones_idusuario(id):
    cnx = conexion_bd()
    cursor = cnx.cursor()

    reservaciones = []

    cursor.execute("SELECT * FROM reservaciones WHERE id_usuario = %s", (id,))
    reservaciones = cursor.fetchall()

    cursor.close()
    cnx.close()

    return reservaciones

def obtener_usuario_username(username):
    cnx = conexion_bd()
    cursor = cnx.cursor()

    perfil = []

    cursor.execute("SELECT id_usuario,nombre,edad,username,ciudad FROM usuarios WHERE username = %s", (username,))
    perfil = cursor.fetchone()

    cursor.close()
    cnx.close()

    return perfil

def obtener_reservaciones_avion(id):
    cnx = conexion_bd()
    cursor = cnx.cursor()

    reservaciones = []

    cursor.execute("SELECT * FROM reservaciones WHERE id_avion = %s", id)
    reservaciones = cursor.fetchall()

    cursor.close()
    cnx.close()

    return reservaciones

def obtener_vuelos():
    cnx = conexion_bd()
    cursor = cnx.cursor()

    vuelos = []

    cursor.execute("SELECT * FROM vuelos")
    vuelos = cursor.fetchall()

    cursor.close()
    cnx.close()

    return vuelos

def obtener_vuelos_fecha(fecha):
    cnx = conexion_bd()
    cursor = cnx.cursor()

    vuelos = []

    cursor.execute("SELECT * FROM vuelos WHERE fecha_vuelo = %s", fecha)
    vuelos = cursor.fetchall()

    cursor.close()
    cnx.close()

    return vuelos

def obtener_vuelos_ciudad(ciudad):
    cnx = conexion_bd()
    cursor = cnx.cursor()

    vuelos = []

    cursor.execute("SELECT * FROM vuelos WHERE ciudad_llegada = %s", ciudad)
    vuelos = cursor.fetchall()

    cursor.close()
    cnx.close()

    return vuelos

#def generar_reservacion():

#def eliminar_reservacion

#def editar_reservacion
