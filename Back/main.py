from flask import Flask, jsonify, request
import modelos

app = Flask(__name__)

@app.route("/api/reservacionesidusuario",methods=["GET"])
def get_reservations_userid():
    userid = request.args.get('id_usuario')
    reservaciones = []
    resultado = modelos.obtener_reservaciones_idusuario(userid)
    claves = ['id_reservacion', 'id_usuario','nombre_persona', 'id_avion', 'id_vuelo', 'asiento', 'fecha_reservacion']

    for objetos in resultado:
        list2dic = dict(zip(claves, objetos))
        reservaciones.append(list2dic)

    return jsonify({"data":reservaciones})

@app.route("/api/informacionusername",methods=["GET"])
def get_user_info():
    username = request.args.get('username')
    informacion_user = []
    resultado = modelos.obtener_usuario_username(username)
    claves = ['id_usuario','nombre','edad','username','ciudad']

    informacion_user = dict(zip(claves, resultado))
    
    return jsonify({"data":informacion_user})

@app.route("/api/reservacionesavion",methods=["GET"])
def get_reservations_plane():
    idavion = request.args.get('id_avion')
    reservaciones = []
    resultado = modelos.obtener_reservaciones_avion(idavion)
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
        list2dic = dict(zip(claves, objetos))
        vuelos.append(list2dic)

    return jsonify({"data":vuelos})

@app.route("/api/vuelosciudad",methods=["GET"])
def get_flys_date():
    ciudad = request.args.get('ciudad')
    vuelos = []
    resultado = modelos.obtener_vuelos_ciudad(ciudad)
    claves = ['id_vuelo', 'id_avion', 'fecha_vuelo', 'hora_estimada', 'asientos_disponibles', 'ciudad_salida', 'ciudad_llegada']

    for objetos in resultado:
        list2dic = dict(zip(claves, objetos))
        vuelos.append(list2dic)

    return jsonify({"data":vuelos})

@app.route("/api/generarreservacion", methods=["POST"])
def add_user():
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

@app.route("/api/editarreservacion/<id>", methods=["PUT"])
def reservation_edit(id):
    nombre = request.json['nombre_persona']
    asiento = request.json['asiento']
    modelos.editar_reservacion(id, nombre, asiento)



if __name__ == '__main__':
    app.run(debug=True, host = "localhost", port=8000)

