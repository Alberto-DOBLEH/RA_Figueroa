from BD import conexion_bd

class Reservaciones:
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

    def obtener_reservaciones_idusuario(self, id):
        try:
            self.conectar()
            self.cursor.execute("SELECT * FROM reservaciones WHERE id_usuario = %s", (id,))
            reservaciones = self.cursor.fetchall()
        finally:
            self.cerrar_conexion()
        return reservaciones

    def obtener_reservaciones_avion(self, id):
        try:
            self.conectar()
            self.cursor.execute("SELECT * FROM reservaciones WHERE id_avion = %s", (id,))
            reservaciones = self.cursor.fetchall()
        finally:
            self.cerrar_conexion()
        return reservaciones

    def generar_reservacion(self, usuario, nombre, vuelo, asiento, fecha_reservacion):
        try:
            self.conectar()
            self.cursor.execute(
                "INSERT INTO reservaciones (id_usuario, nombre_persona, id_vuelo, asiento, fecha_reservacion) "
                "VALUES (%s, %s, %s, %s, %s)",
                (usuario, nombre, vuelo, asiento, fecha_reservacion)
            )
            self.cnx.commit()
        finally:
            self.cerrar_conexion()

    def eliminar_reservacion(self, id_reservacion):
        try:
            self.conectar()
            self.cursor.execute("DELETE FROM reservaciones WHERE id_reservacion = %s", (id_reservacion,))
            self.cnx.commit()
        finally:
            self.cerrar_conexion()

    def editar_reservacion(self, id_reservacion, nombre=None, asiento=None):
        try:
            self.conectar()
            if nombre is not None:
                self.cursor.execute(
                    "UPDATE reservaciones SET nombre_persona = %s WHERE id_reservacion = %s",
                    (nombre, id_reservacion)
                )
            if asiento is not None:
                self.cursor.execute(
                    "UPDATE reservaciones SET asiento = %s WHERE id_reservacion = %s",
                    (asiento, id_reservacion)
                )
            self.cnx.commit()
        finally:
            self.cerrar_conexion()

