from BD import conexion_bd

class Aviones:
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

    def agregar_avion(self, modelo, fecha_adquisicion, ultimo_chequeo, cantidad_asientos):
        try:
            self.conectar()
            self.cursor.execute(
                "INSERT INTO aviones (modelo, fecha_adquisicion, ultimo_chequeo, cantidad_asientos) "
                "VALUES (%s, %s, %s, %s)",
                (modelo, fecha_adquisicion, ultimo_chequeo, cantidad_asientos)
            )
            self.cnx.commit()
        finally:
            self.cerrar_conexion()

    def eliminar_avion(self, id):
        try:
            self.conectar()
            self.cursor.execute(
                "DELETE FROM aviones WHERE id_avion = %s",
                (id,)
            )
            self.cnx.commit()
        finally:
            self.cerrar_conexion()

    def actualizar_ultimo_chequeo(self, id, fecha_chequeo):
        try:
            self.conectar()
            self.cursor.execute(
                "UPDATE aviones SET ultimo_chequeo = %s WHERE id_avion = %s",
                (fecha_chequeo, id)
            )
            self.cnx.commit()
        finally:
            self.cerrar_conexion()
