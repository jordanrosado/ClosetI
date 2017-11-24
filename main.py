import time
import sys
import os
import subprocess
import mysql.connector
import json
import numpy as np

from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3
from colorthief import ColorThief
from cv2 import *
from PIL import Image
from flask import *
from Clasificador import piClasificador

clas = piClasificador()

app = Flask(__name__)

@app.route("/")
def main():
	cnx = mysql.connector.connect(user='addy', password='hola1234', host='localhost', database='test')
	cursor = cnx.cursor()
	sql = "SELECT * FROM clothes WHERE tipo='top'"
	cursor.execute(sql)			
	resultados = cursor.fetchall()
	sql2 = "SELECT * FROM clothes WHERE tipo='pantalon'"	
	cursor.execute(sql2)
	resultadosDos = cursor.fetchall()
	cache = time.time()
	return render_template('index.html', results=resultados, resultsDos=resultadosDos, cacheWeb = cache)

@app.route("/camera", methods=['POST'])
def camera():

	   print("Inicio proceso Camara")
	   #subprocess.call(['python','/home/pi/webapp/motorFoto.py'])
	   print("Fin proceso Camara")

	   slotdis = encontrarSlot()
	   print("SLOT=" + str(slotdis))
           #Codigo para mover a posicion de toma de foto
           clas.agregar(slotdis, take(slotdis))
	   print("Fin proceso Camera")

	   #subprocess.call(['python','/home/pi/webapp/moverRiel.py'])
	   #subprocess.call(['python','/home/pi/webapp/motorSlot.py',format(slotdis)])
	   #Codigo servomotor y motor DC
	   #subprocess.call(['python','/home/pi/webapp/servo.py'])
	   #time.sleep(3)
	   #subprocess.call(['python','/home/pi/webapp/motorRegresar.py',format(slotdis)])	
	   return 'OK'
	   

@app.route("/dispensar/<int:slot>", methods=['POST'])
def dispensar(slot):
	   #Codigo para sacar ropa
	   delete(slot) 
	   eliminar_slot(slot)	
	   print("Eliminar")
	   return 'OK'
	   #Codigo para mover a posicion del slot






























def eliminar_slot(slot):
	conn = mysql.connector.connect(user='addy', password='hola1234',
	                              host='localhost',
	                              database='test')
	cur = conn.cursor()
	cur.execute("""DELETE FROM clothes WHERE slot = '%s'""",(slot,))
	conn.commit()
	cur.close()
	conn.close()

def take(variable):
	while validar(variable)==1:
            cam = VideoCapture(-1)
	    cam.set(3,1280)
  	    cam.set(4,720)
	    time.sleep(2)

            s, img = cam.read()
            if s:
               waitKey(30) 
               imwrite("/home/pi/webapp/static/themes/images/clothes/"+ str(variable) +".jpg",img)
               cam.release()
	    time.sleep(1)
	    cam.release()
	return str(variable) +".jpg"	
        
def delete(value):
	while validar(value)==0:
            try:
                os.remove("/home/pi/webapp/static/themes/images/clothes/" + str(value) +".jpg")
                print("true")
            except:
                print("false")
                pass
	
	
def validar(slot):
	archivo = "/home/pi/webapp/static/themes/images/clothes/"+ str(slot) +".jpg"
	try:
    	    with open(archivo, 'r') as file:
        	file = file.read()
		return 0
	except:
	    pass
    	    return 1

def encontrarSlot():
	conn = mysql.connector.connect(user='addy', password='hola1234',
			                      host='localhost',
			                      database='test')
	cur = conn.cursor(buffered=True)
	## obtener datos
	cur.execute("SELECT slot, tipo,color FROM clothes")
	row = cur.fetchone()
	slot_buscado = 1
	flag = 0
	while row is not None:
	    if(slot_buscado==row[0]):
		slot_buscado=slot_buscado+1
	    else:
		buscado = slot_buscado
		flag = 1
		break
	    row = cur.fetchone()
	if flag == 0:
		buscado = slot_buscado
	cur.close()
	conn.close()
	return buscado


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

