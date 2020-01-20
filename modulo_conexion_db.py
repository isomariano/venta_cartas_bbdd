import pymysql
from modulo_genera_registros import *

class DataBase:
	def __init__(self):
		self.connection = pymysql.connect(
			host = "localhost", 
			user = "root", 
			password = "", 
			db = "mtg ventas"
			)
		self.cursor = self.connection.cursor()
		print ("conexion establecida")

	def select_cartas (self, accion):

		if accion == "todas":
			sql1 = "SELECT * FROM tabla_cartas ORDER BY TIPO"
			sql2 = "SELECT SUM(PRECIO_DOLARES), SUM(COMISION), SUM(PARTE_TIENDA), SUM(TOTAL) FROM tabla_cartas"
		else:
			sql1 = "SELECT * FROM tabla_cartas WHERE ESTADO = '{}' ORDER BY TIPO".format(accion)
			sql2 = "SELECT SUM(PRECIO_DOLARES), SUM(COMISION), SUM(PARTE_TIENDA), SUM(TOTAL) FROM tabla_cartas WHERE ESTADO = '{}'".format(accion)

		try:
			self.cursor.execute(sql1)
			cartas = self.cursor.fetchall()
			print (" ESTADO      DOLARES     PESOS        CARTA")

			for carta in cartas:
				print (carta [5], "\t", "U$S", carta [1], "\t", "$", carta[4], "\t", carta [0])

			self.cursor.execute(sql2)
			totales = self.cursor.fetchone()
			print ("TOTAL U$S: ", totales [0], "TOTAL $: ", totales[3], "TOTAL COMISION $: ", totales [1])
		except:
			raise

	def select_carta(self, nombre):
		sql = "SELECT * FROM tabla_cartas WHERE NOMBRE = '{}' ORDER BY TIPO".format(nombre)

		try:
			self.cursor.execute(sql)
			carta = self.cursor.fetchone()
			print (" ESTADO      DOLARES     PESOS        CARTA")
			print (carta [5], "\t", "U$S", carta [1], "\t", "$", carta[4], "\t", carta [0])
		except:
			raise
		


	def close(self):
		self.connection.close()

def main():  #llama a la funcion de conexion con la bbdd y recursividad
	
	accion = input ("mostrar cartas (todas/vendido/disponible): ")
	print ()
	mi_db = DataBase()
	mi_db.select_cartas(accion)
	mi_db.close()

	recursividad = input ("desea realizar otra accion? ")
	print ()
	if recursividad == "si":
		main()

if __name__ == "__main__":
	main()