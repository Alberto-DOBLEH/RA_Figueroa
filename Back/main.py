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



if __name__ == '__main__':
    app.run(debug=True, host = "localhost", port=8000)

