from BD import conexion_bd

class Vuelos:
    def __init__(self):
        self.cnx = None
        self.cursor = None

    def conectar(self):
        self.cnx = conexion_bd()
        self.cursor = self.cnx.cursor()

    def cerrar_conexion(self):
        if self.cursor:
            self.cursor.close()
        if self.cnx:
            self.cnx.close()

    def obtener_vuelos(self):
        try:
            self.conectar()
            self.cursor.execute("SELECT * FROM vuelos")
            vuelos = self.cursor.fetchall()
        finally:
            self.cerrar_conexion()
        return vuelos

    def obtener_vuelos_por_fecha(self, fecha):
        try:
            self.conectar()
            self.cursor.execute("SELECT * FROM vuelos WHERE fecha_vuelo = %s", (fecha,))
            vuelos = self.cursor.fetchall()
        finally:
            self.cerrar_conexion()
        return vuelos

    def obtener_vuelos_por_ciudad(self, ciudad):
        try:
            self.conectar()
            self.cursor.execute("SELECT * FROM vuelos WHERE ciudad_llegada = %s", (ciudad,))
            vuelos = self.cursor.fetchall()
        finally:
            self.cerrar_conexion()
        return vuelos

    def modificar_vuelo_fecha_hora(self, id, fecha, hora):
        try:
            self.conectar()
            self.cursor.execute(
                "UPDATE vuelos SET fecha = %s, hora = %s WHERE id_vuelo = %s",
                (fecha, hora, id)
            )
            self.cnx.commit()
        finally:
            self.cerrar_conexion()

    def modificar_avion(self, id, modelo, ultimo_chequeo, cantidad_asientos):
        try:
            self.conectar()
            self.cursor.execute(
                "UPDATE aviones SET modelo = %s, ultimo_chequeo = %s, cantidad_asientos = %s WHERE id_avion = %s",
                (modelo, ultimo_chequeo, cantidad_asientos, id)
            )
            self.cnx.commit()
        finally:
            self.cerrar_conexion()

    def eliminar_vuelo(self, id):
        try:
            self.conectar()
            self.cursor.execute("DELETE FROM vuelos WHERE id_vuelo = %s", (id,))
            self.cnx.commit()
        finally:
            self.cerrar_conexion()
