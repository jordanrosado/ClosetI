import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3
from colorthief import ColorThief
import mysql.connector

class piBase(object):
    def _init_(self):
        pass


    def encontrar_slot(self):
	conn = mysql.connector.connect(user='addy', password='hola1234',
	                              host='localhost',
	                              database='test')
	cur = conn.cursor()
	
	## obtener datos
	cur.execute("SELECT slot, tipo,color FROM clothes")
	row = cur.fetchone()
	slot_buscado = 1
	flag = 0
	while row is not None:
	    if(c==row[0]):
		slot_buscado=slot_buscado+1
	    else:
	    	buscado = c
		flag = 1
		break
	    row = cur.fetchone()
	if flag == 0:
		buscado = slot_buscado
	cur.close()
	conn.close()
	return buscado

    def classify_color(direccion):
	color_thief = ColorThief(direccion)
	# build a color palette
	palette = color_thief.get_palette(color_count=6)
	#print palette
	color_rgb = palette[1]
	c = etiquetado(color_rgb)
	return c;
