#modulo para ingresar registros en la base de datos primerabbdd
import sqlite3
from modulo_genera_registros import *

def conexion_bbdd(opcion_elegida): #conexion a bbdd para realizar consultas o ingresar registros

	miconexion = sqlite3.connect("primerabbdd")
	micursor = miconexion.cursor()

	if opcion_elegida == "consulta":
		micursor.execute("SELECT * FROM CARTAS")
		registros = micursor.fetchall()
		for registro in registros:
			print("carta: " + str(registro))

	elif opcion_elegida == "ingreso":
		registros_recibidos = envia_registros()  #se llama a la funcion del modulo_genera_registros
		micursor.executemany("INSERT INTO CARTAS VALUES (?, ?, ?, ?, ?, ?)", registros_recibidos)

	print ()
	miconexion.commit()
	miconexion.close()

def main():  #llama a la funcion de conexion con la bbdd y recursividad
	
	accion = input ("consulta o ingreso de datos? ")
	print ()
	conexion_bbdd (accion)

	recursividad = input ("desea realizar otra accion? ")
	print ()
	if recursividad == "si":
		main()

if __name__ == "__main__":
	contraseña = input ("contraseña: ")
	if contraseña == "alojomora":
		print ("contraseña correcta")
		print ()
		main()