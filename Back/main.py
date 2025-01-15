from flask import Flask, jsonify, request
import modelos
from datetime import timedelta

app = Flask(__name__)

@app.route("/api/reservacionesidusuario/<int:id>",methods=["GET"])
def get_reservations_userid(id):
    reservaciones = []
    resultado = modelos.obtener_reservaciones_idusuario(id)
    claves = ['id_reservacion', 'id_usuario','nombre_persona', 'id_avion', 'id_vuelo', 'asiento', 'fecha_reservacion']

    for objetos in resultado:
        list2dic = dict(zip(claves, objetos))
        reservaciones.append(list2dic)

    print("Prueba")
    return jsonify({"data":reservaciones})

@app.route("/api/informacionusername/<username>",methods=["GET"])
def get_user_info(username):
    informacion_user = []
    resultado = modelos.obtener_usuario_username(username)
    claves = ['id_usuario','nombre','edad','username','password','ciudad']

    informacion_user = dict(zip(claves, resultado))
    
    return jsonify({"data":informacion_user})   

@app.route("/api/reservacionesavion/<id>",methods=["GET"])
def get_reservations_plane(id):
    reservaciones = []
    resultado = modelos.obtener_reservaciones_avion(id)
    claves = ['id_reservacion', 'id_usuario','nombre_persona', 'id_avion', 'id_vuelo', 'asiento', 'fecha_reservacion']

    for objetos in resultado:
        list2dic = dict(zip(claves, objetos))
        reservaciones.append(list2dic)
    
    return ({"data": reservaciones})

@app.route("/api/vuelosglobales",methods=["GET"])
def get_flys():
    vuelos = []
    resultado = modelos.obtener_vuelos()
    claves = ['id_vuelo', 'id_avion', 'fecha_vuelo', 'hora_estimada', 'asientos_disponibles', 'ciudad_salida', 'ciudad_llegada']

    
    for objetos in resultado:

        objetos = list(objetos)
        if isinstance(objetos[3], timedelta):  # Suponiendo que `hora_estimada` está en la posición 3
            objetos[3] = str(objetos[3])

        list2dic = dict(zip(claves, objetos))
        vuelos.append(list2dic)

    return jsonify({"data":vuelos})

@app.route("/api/vuelosfechas",methods=["GET"])
def get_flys_date():
    fecha = request.args.get('fecha')
    vuelos = []
    resultado = modelos.obtener_vuelos_fecha(fecha)
    claves = ['id_vuelo', 'id_avion', 'fecha_vuelo', 'hora_estimada', 'asientos_disponibles', 'ciudad_salida', 'ciudad_llegada']

    for objetos in resultado:

        objetos = list(objetos)
        if isinstance(objetos[3], timedelta):  # Suponiendo que `hora_estimada` está en la posición 3
            objetos[3] = str(objetos[3])

        list2dic = dict(zip(claves, objetos))
        vuelos.append(list2dic)

    return jsonify({"data":vuelos})

@app.route("/api/vuelosciudad",methods=["GET"])
def get_flys_city():
    ciudad = request.args.get('ciudad')
    vuelos = []
    resultado = modelos.obtener_vuelos_ciudad(ciudad)
    claves = ['id_vuelo', 'id_avion', 'fecha_vuelo', 'hora_estimada', 'asientos_disponibles', 'ciudad_salida', 'ciudad_llegada']

    for objetos in resultado:

        objetos = list(objetos)
        if isinstance(objetos[3], timedelta):  # Suponiendo que `hora_estimada` está en la posición 3
            objetos[3] = str(objetos[3])

        list2dic = dict(zip(claves, objetos))
        vuelos.append(list2dic)

    return jsonify({"data":vuelos})

@app.route("/api/generarreservacion", methods=["POST"])
def add_reservation():
    usuario = request.json['usuario']
    nombre = request.json['nombre']
    vuelo = request.json['id_vuelo']
    asiento = request.json['asiento']
    fecha_reservacion = request.json['fecha']

    modelos.generar_reservacion(usuario, nombre, vuelo, asiento, fecha_reservacion)

    reservation_dict = {
        "usuario": usuario,
        "nombre": nombre,
        "vuelo": vuelo,
        "asiento": asiento,
        "fecha_reservacion": fecha_reservacion,
    }

    return jsonify(reservation_dict)

@app.route("/api/eliminarreservacion/<id>", methods=["DELETE"])
def reservation_delete(id):
    modelos.eliminar_reservacion(id)
    reservation_dict = {
        'id': id
    }

    return jsonify(reservation_dict)

@app.route("/api/editarreservacion/<int:id>", methods=["PUT"])
def reservation_edit(id):

    if not request.json:
        return jsonify({"message": "Datos inválidos, no se encontró el JSON en la solicitud"}), 400

    if 'nombre_persona' not in request.json or 'asiento' not in request.json:
        return jsonify({"message": "Faltan campos en la solicitud"}), 400

    datos = request.json
    nombre = request.json.get('nombre_persona')
    asiento = request.json.get('asiento')

    modelos.editar_reservacion(id, nombre, asiento)

    return jsonify({"message": "Reservación actualizada correctamente"}), 200

@app.route("/api/agregarusuario", methods=["POST"])
def add_user():
    
    nombre = request.json['nombre']
    edad = request.json['edad']
    usuario = request.json['usuario']
    contraseña = request.json['contraseña']
    ciudad = request.json['ciudad']

    modelos.agregar_usuario(nombre, edad, usuario, contraseña, ciudad)

    datos_dict={
        'nombre' : nombre,
        'edad' : edad,
        'usuario' : usuario,
        'contraseña' : contraseña,
        'ciudad' : ciudad
    }

    return jsonify(datos_dict,{"message": "Usuario creado correctamente"}), 200

@app.route("/api/editarusuario/<int:id>", methods=["PUT"])
def user_edit(id):

    data = request.json

    nombre = request.data.get('nombre')
    username = request.data.get('username')
    contraseña = request.data.get('contraseña')
    ciudad = request.data.get('ciudad')

    modelos.modificar_usuario(id, nombre, username, contraseña, ciudad)

    return jsonify({"message": "Usuario actualizado correctamente"}), 200

@app.route("/api/eliminarusuario/<id>", methods=["DELETE"])
def user_delete(id):
    modelos.eliminar_usuario(id)
    return jsonify({"message": "Usuario Eliminado"}), 200

@app.route("/api/editarvuelo/<int:id>", methods=["PUT"])
def fly_edit(id):

    data = request.json

    fecha = request.data.get('fecha')
    hora = request.data.get('hora')

    modelos.modificar_vuelos(id, fecha, hora)

    return jsonify({"message": "Vuelo actualizado correctamente"}), 200

@app.route("/api/eliminarvuelo/<id>", methods=["DELETE"])
def fly_delete(id):
    modelos.eliminar_vuelo(id)
    return jsonify({"message": "Vuelo Eliminado"}), 200

@app.route("/api/agregaravion", methods=["POST"])
def add_plane():
    
    modelo = request.json['modelo']
    fecha_adquisicion = request.json['fecha_adquisicion']
    ultimo_chequeo = request.json['ultimo_chequeo']
    cantidad_asientos = request.json['cantidad_asientos']

    modelos.agregar_avion(modelo, fecha_adquisicion, ultimo_chequeo, cantidad_asientos)

    return jsonify({"message": "Avion agregado correctamente"}), 200

@app.route("/api/editaravion/<int:id>", methods=["PUT"])
def plane_edit(id):

    data = request.json

    modelo = request.data.get('modelo')
    ultimo_chequeo = request.data.get('ultimo_chequeo')
    asientos = request.data.get('asientos')

    modelos.modificar_vuelos(id, modelo , ultimo_chequeo, asientos)

    return jsonify({"message": "Avion actualizado correctamente"}), 200

@app.route("/api/eliminaravion/<id>", methods=["DELETE"])
def plane_delete(id):
    modelos.eliminar_aviones(id)
    return jsonify({"message": "Avion Eliminado"}), 200


if __name__ == '__main__':
    app.run(debug=True, host = "localhost", port=8000)

