from BD import conexion_bd

#Se usa para obtener todas las reservaciones globales
def obtener_reservaciones():
    cnx = conexion_bd()
    cursor = cnx.cursor()

    reservaciones = []

    cursor.execute("SELECT * FROM reservaciones")
    reservaciones = cursor.fetchall()

    cnx.close()
    cursor.close()

    return reservaciones

#Se usa para obtener las reservaciones por usuario por medio de su id
def obtener_reservaciones_idusuario(id):
    cnx = conexion_bd()
    cursor = cnx.cursor()

    reservaciones = []

    cursor.execute("SELECT * FROM reservaciones WHERE id_usuario = %s", id)
    reservaciones = cursor.fetchone()

    cnx.close()
    cursor.close()

    return reservaciones

def obtener_usuario_username(username):
    cnx = conexion_bd()
    cursor = cnx.cursor()

    perfil = []

    cursor.execute("SELECT * FROM usuarios WHERE username = %s", username)
    perfil = cursor.fetchone()

    cnx.close()
    cursor.close()

    return perfil

def obtener_reservaciones_avion(id):
    cnx = conexion_bd()
    cursor = cnx.cursor()

    reservaciones = []

    cursor.execute("SELECT * FROM reservaciones WHERE id_avion = %s", id)
    reservaciones = cursor.fetchone()

    cnx.close()
    cursor.close()

    return reservaciones

#def obtener_vuelos():

#def obtener_vuelos_fecha():

#def obtener_vuelos_ciudad():

