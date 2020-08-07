import sqlite3
conexion = sqlite3.connect("sqlite3/sistemaApuestasBD.sqlite3")
consulta = conexion.cursor()

crear_tabla_usuario = """
CREATE TABLE IF NOT EXISTS USUARIO(
    idusuario INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre_usuario  VARCHAR(50) NOT NULL,
    contraseña_usuario  VARCHAR(8) NOT NULL
)"""
consulta.execute(crear_tabla_usuario)

crear_tabla_equipo  = """
CREATE TABLE IF NOT EXISTS EQUIPO(
    idequipo INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre_equipo VARCHAR(50) NOT NULL
)"""
consulta.execute(crear_tabla_equipo)
crear_tabla_apuestas = """
CREATE TABLE IF NOT EXISTS APUESTAS(
    idapuestas INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    idusuario INTEGER UNSIGNED NOT NULL,
    idequipo  INTEGER UNSIGNED NOT NULL,
    FOREIGN KEY (idusuario) REFERENCES USUARIO (idusuario) 
	    ON DELETE RESTRICT ON UPDATE NO ACTION,
	FOREIGN KEY (idequipo) REFERENCES EQUIPO (idequipo) 
	    ON DELETE RESTRICT ON UPDATE NO ACTION
)"""
consulta.execute(crear_tabla_apuestas)
consulta.close()
conexion.commit()
conexion.close()