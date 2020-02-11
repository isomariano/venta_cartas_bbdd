#modulo principal que permite elegir las acciones a realizar,
# crea la conexion a la bbdd y llama a los metodos del otro modulo
from modulo_conexion_db import *

def main():
	
	print ("acciones a realizar: \n - todas: muestra todas las cartas\n", 
		"- vendido: muestra las cartas que se hayan vendido\n", 
		"- disponible: muestra las cartas que se encuentren disponibles\n", 
		"- especifica: muestra la carta que se especifique\n", 
		"- ingreso: para ingresar cartas a la base de datos\n", 
		"- actualizar: cambia el estado de una carta vendido/disponible")
	print ()
	accion = input ("accion a realizar: ")
	print ()
	mi_db = data_base()

	if accion == "ingreso":
		mi_db.ingreso_cartas()
		mi_db.commit()
	elif accion == "actualizar":
		mi_db.actualiza_estado()
		mi_db.commit()
	else:
		mi_db.consulta_cartas(accion)
	mi_db.close()

	recursividad = input ("realizar otra accion? ")
	print ()
	if recursividad == "si":
		main()

if __name__ == "__main__":
	main()