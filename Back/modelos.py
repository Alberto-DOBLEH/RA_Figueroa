from BD import conexion_bd

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

    cursor.execute("SELECT * FROM reservaciones WHERE id_avion = %s", (id,))
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

    cursor.execute("SELECT * FROM vuelos WHERE fecha_vuelo = %s", (fecha,))
    vuelos = cursor.fetchall()

    cursor.close()
    cnx.close()

    return vuelos

def obtener_vuelos_ciudad(ciudad):
    cnx = conexion_bd()
    cursor = cnx.cursor()

    vuelos = []

    cursor.execute("SELECT * FROM vuelos WHERE ciudad_llegada = %s", (ciudad,))
    vuelos = cursor.fetchall()

    cursor.close()
    cnx.close()

    return vuelos

def generar_reservacion(usuario, nombre, vuelo, asiento, fecha_reservacion):
    cnx = conexion_bd()
    cursor = cnx.cursor()


    cursor.execute("INSERT INTO reservaciones(id_usuario, nombre_persona, id_vuelo, asiento, fecha_reservacion) VALUES (%s,%s,%s,%s,%s)", (usuario, nombre, vuelo, asiento, fecha_reservacion))
    cnx.commit()

    cursor.close()
    cnx.close()

def eliminar_reservacion(reservacion):
    cnx = conexion_bd()
    cursor = cnx.cursor()

    cursor.execute("DELETE FROM reservaciones WHERE id_reservacion = %s"(reservacion,))
    cnx.commit()

    cursor.close()
    cnx.close()

def editar_reservacion(reservacion, nombre, asiento):
    cnx = conexion_bd()
    cursor = cnx.cursor()

    if(nombre is None):
        cursor.execute("UPDATE ON reservaciones SET asiento = %s WHERE id_reservacion = %s"(asiento, reservacion))
        cnx.commit()
    
    if(asiento is None):
        cursor.execute("UPDATE ON reservaciones SET nombre_persona = %s WHERE id_reservacion = %s"(nombre, reservacion))
        cnx.commit()

    cursor.close()
    cnx.close()

#AGREGAR USUARIO

#MODIFICAR USUARIO

#ELIMINAR USUARIO

#MODIFICAR VUELOS

#ELIMINAR VUELOS

#AGREGAR AVIONES

#MODIFICAR AVIONES

#ELIMINAR AVIONES
