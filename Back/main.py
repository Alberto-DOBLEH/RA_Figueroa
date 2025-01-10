from flask import Flask, jsonify, request
import modelos

app = Flask(__name__)

@app.route("/api/reservacionesglobales", methods=["GET"])
def get_reservations():
    reservaciones = []
    resultado = modelos.obtener_reservaciones()
    claves = ['id_reservacion', 'id_usuario', 'id_avion', 'id_vuelo', 'asiento', 'fecha_reservacion']

    for objetos in resultado:
        list2dic = dict(zip(claves, objetos)) #convertimos la tupla result y la lista claves en un diccionario
        reservaciones.append(list2dic)

    return jsonify({"data":reservaciones})





if __name__ == '__main__':
    app.run(debug=True, host = "localhost", port=8000)

