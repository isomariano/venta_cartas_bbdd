# modulo que contiene la clase DataBase para conectar con la bbdd MySQL
# y los metodos para poder manipularla
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

	def commit(self):
		self.connection.commit()

	def close(self):
		self.connection.close()

	def select_cartas (self, accion): #consulta de los registros total o filtrada por estado

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

	def select_carta(self): #consulta especifica
		nombre = input("nombre de la carta: ")
		sql = "SELECT * FROM tabla_cartas WHERE NOMBRE = '{}' ORDER BY TIPO".format(nombre)

		try:
			self.cursor.execute(sql)
			carta = self.cursor.fetchone()
			print (" ESTADO      DOLARES     PESOS        CARTA")
			print (carta [5], "\t", "U$S", carta [1], "\t", "$", carta[4], "\t", carta [0])
		except:
			print ("carta no encontrada")
		
	def ingreso_cartas(self): #ingresa registros a la bbdd
		registros_recibidos = envia_registros()  #se llama a la funcion del modulo_genera_registros
		
		sql = "INSERT INTO tabla_cartas VALUES (%s, %s, %s, %s, %s, %s, %s)"
		try:
			self.cursor.executemany(sql, registros_recibidos)
			print ("cartas ingresadas con exito")
		except:
			print ("ha ocurrido un error")
			raise

	def actualizar(self): #cambiar el estado de un registro vendido/disponible
		nombre, estado = input("nombre: "), input ("cambio a vendido/disponible: ")

		sql = "UPDATE tabla_cartas set ESTADO = '{}' WHERE NOMBRE = '{}'".format(estado, nombre)
		try:
			self.cursor.execute(sql)
		except:
			print ("carta no encontrada")