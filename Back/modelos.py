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

    cursor.execute("SELECT * FROM usuarios WHERE username = %s", (username,))
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

    cursor.execute("DELETE FROM reservaciones WHERE id_reservacion = %s",(reservacion,))
    cnx.commit()

    cursor.close()
    cnx.close()

def editar_reservacion(id, nombre, asiento):

    cnx = conexion_bd()
    cursor = cnx.cursor()

    cursor.execute("UPDATE reservaciones SET nombre_persona = %s, asiento = %s WHERE (id_reservacion = %s)",(nombre, asiento, id))

    if cursor.rowcount == 0:
        return "No se encontró la reservación con el ID proporcionado", 404

    cnx.commit()

    cursor.close()
    cnx.close()

#AGREGAR USUARIO
def agregar_usuario(nombre, edad, username, contraseña, ciudad):
    cnx = conexion_bd()
    cursor = cnx.cursor()
    
    cursor.execute("INSERT INTO usuarios(nombre, edad, username, contraseña, ciudad) VALUES (%s,%s,%s,%s,%s)", (nombre, edad, username, contraseña, ciudad))
    cnx.commit()

    cursor.close()
    cnx.close()

#MODIFICAR USUARIO
def modificar_usuario(id, nombre, username, contraseña, ciudad):
    cnx = conexion_bd()
    cursor = cnx.cursor()

    cursor.execute("UPDATE usuarios SET nombre = %s, username = %s, contraseña = %s, ciudad = %s WHERE id_usuario = %s",(nombre, username, contraseña, ciudad, id))
    cnx.commit()

    cursor.close()
    cnx.close()

#ELIMINAR USUARIO
def eliminar_usuario(id):
    cnx = conexion_bd()
    cursor = cnx.cursor()

    cursor.execute("DELETE FROM usuarios WHERE id_usuario = %s",(id,))
    cnx.commit()

    cursor.close()
    cnx.close()

#MODIFICAR VUELOS
def modificar_vuelos(id, fecha, hora):
    cnx = conexion_bd()
    cursor = cnx.cursor()
    
    cursor.execute("UPDATE vuelos SET fecha = %s, hora = %s WHERE id_vuelo = %s",(fecha, hora, id))
    cnx.commit()

    cursor.close()
    cnx.close()

#ELIMINAR VUELOS
def eliminar_vuelo(id):
    cnx = conexion_bd()
    cursor = cnx.cursor()

    cursor.execute("DELETE FROM vuelos WHERE id_vuelo = %s",(id,))
    cnx.commit()

    cursor.close()
    cnx.close()

#AGREGAR AVIONES
def agregar_avion(modelo, fecha_adquisicion, ultimo_chequeo, cantidad_asientos):
    cnx = conexion_bd()
    cursor = cnx.cursor()

    cursor.execute("INSERT INTO aviones(modelo, fecha_adquisicion, ultimo_chequeo, cantidad_asientos) VALUES (%s,%s,%s,%s)", (modelo, fecha_adquisicion, ultimo_chequeo, cantidad_asientos))
    cnx.commit()

    cursor.close()
    cnx.close()

#MODIFICAR AVIONES
def modificar_vuelos(id, modelo , ultimo_chequeo, asientos):
    cnx = conexion_bd()
    cursor = cnx.cursor()
    
    cursor.execute("UPDATE aviones SET modelo = %s, ultimo_chequeo = %s, cantidad_asientos = %s WHERE id_avion = %s",(modelo, ultimo_chequeo, asientos, id))
    cnx.commit()

    cursor.close()
    cnx.close()

#ELIMINAR AVIONES
def eliminar_aviones(id):
    cnx = conexion_bd()
    cursor = cnx.cursor()

    cursor.execute("DELETE FROM aviones WHERE id_avion = %s",(id,))
    cnx.commit()

    cursor.close()
    cnx.close()