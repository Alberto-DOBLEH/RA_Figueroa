from BD import conexion_bd

class Usuarios:
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

    def obtener_usuario_username(self, username):
        try:
            self.conectar()
            self.cursor.execute(
                "SELECT id_usuario, nombre, edad, username, ciudad FROM usuarios WHERE username = %s",
                (username,)
            )
            perfil = self.cursor.fetchone()
        finally:
            self.cerrar_conexion()
        return perfil

    def agregar_usuario(self, nombre, edad, username, contrasena, ciudad):
        try:
            self.conectar()
            self.cursor.execute(
                "INSERT INTO usuarios (nombre, edad, username, contrasena, ciudad) "
                "VALUES (%s, %s, %s, %s, %s)",
                (nombre, edad, username, contrasena, ciudad)
            )
            self.cnx.commit()
        finally:
            self.cerrar_conexion()

    def eliminar_usuario(self, id):
        try:
            self.conectar()
            self.cursor.execute(
                "DELETE FROM usuarios WHERE id_usuario = %s",
                (id,)
            )
            self.cnx.commit()
        finally:
            self.cerrar_conexion()

    def modificar_usuario(self, id, nombre=None, username=None, contrasena=None, ciudad=None):
        try:
            self.conectar()
            campos = []
            valores = []

            if nombre is not None:
                campos.append("nombre = %s")
                valores.append(nombre)

            if username is not None:
                campos.append("username = %s")
                valores.append(username)

            if contrasena is not None:
                campos.append("contrasena = %s")
                valores.append(contrasena)

            if ciudad is not None:
                campos.append("ciudad = %s")
                valores.append(ciudad)

            if campos:
                query = f"UPDATE usuarios SET {', '.join(campos)} WHERE id_usuario = %s"
                valores.append(id)
                self.cursor.execute(query, valores)
                self.cnx.commit()
        finally:
            self.cerrar_conexion()