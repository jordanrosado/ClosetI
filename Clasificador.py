import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3
from colorthief import ColorThief
import mysql.connector


class piClasificador(object):
    def _init_(self):
        pass
    
    def etiquetado(self,rgb_tuple):
	colors = {'rojo': (255,0,0),
		  'verde': (0,255,0),
		  'azul': (0,0,255),
		  'amarillo': (255,255,0),
		  'naranja': (255,127,0),
		  'blanco': (255,255,255),
		  'negro': (0,0,0),
		  'gris': (127,127,127),
		  'rosa': (255,127,127),
		  'morado': (127,0,255)}

	manhattan = lambda x,y : abs(x[0] - y[0]) + abs(x[1] - y[1]) + abs(x[2] - y[2]) 
	distances = {k: manhattan(v, rgb_tuple) for k, v in colors.items()}
	color = min(distances, key=distances.get)
	return color

	# clasificacion por color
    def classify_color(self, direccion):
	 color_thief = ColorThief(direccion)
	# build a color palette
	 palette = color_thief.get_palette(color_count=6)
	 print palette
	#print palette
	 color_rgb = palette[1]
	 return self.etiquetado(color_rgb)

    ##CLASIFICACION POR TIPO
    def classifyTipo (self,direccion):
	 visual_recognition = VisualRecognitionV3(VisualRecognitionV3.latest_version,api_key='c4fac6f28d88796dfcef6f28faf3e34cf034a788')
		 
	 with open(join(dirname(__file__), direccion), 'rb') as image_file:  
			obj = visual_recognition.classify(images_file=image_file, threshold=0, classifier_ids=['Closet_242106109'])
		 ##JSONObject x = (obj) JSONValue.parse(jsonString);
	 x = json.dumps(obj, indent = 2)
		#print(x)
	 xstr = json.loads(x)
	 lista = xstr['images']
		# volvemos diccionario
	 ystr=lista.pop(0)
	 lista2 = ystr['classifiers']
	 zstr = lista2.pop(0)
         lista3 = zstr['classes']
	 obja = lista3.pop(0); #{u'score': 9.37017e-05, u'class': u'blusas'}
	 score_top= obja['score']
	 objb = lista3.pop(0)
	 score_bottom = objb['score']
	 if(score_top>score_bottom):
	    tipo = "top"
   	 else:
	    tipo="pantalon"
	 return tipo

    def agregar(self,slot,direccion):
	 color= self.classify_color(direccion)
	 tipo = self.classifyTipo (direccion)
	 cnx = mysql.connector.connect(user='addy', password='hola1234',
			                      host='localhost',
			                      database='test')
	
	 cursor = cnx.cursor()
	 cursor.execute("""INSERT into clothes (slot, tipo,color,url)
			          values (%s, %s,%s,%s)""",
			          (slot,tipo,color,direccion))
	
	 cnx.commit()
	 cursor.close()
	 cnx.close()
	 return 1


    def eliminar_slot(self, slot):
	conn = mysql.connector.connect(user='addy', password='hola1234',
	                              host='localhost',
	                              database='test')
	cur = conn.cursor()
	cur.execute("""DELETE FROM clothes WHERE slot = '%s'""",(slot,))
	conn.commit()
	cur.close()
	conn.close()
	
