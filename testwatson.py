import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3
from colorthief import ColorThief
import mysql.connector
visual_recognition = VisualRecognitionV3(VisualRecognitionV3.latest_version,api_key='c4fac6f28d88796dfcef6f28faf3e34cf034a788')
direccion = "/home/pi/webapp/clothes/29.jpg"		 
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
	print ( "top")
else:
	print ("pantalon")


  