from cv2 import *
from PIL import Image
import time
import sys
import os

class piCamera(object):
    def _init_(self):
        pass
    
    def take(self, variable):
	while self.validar(variable)==1:
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
        
    def delete(self, value):
	while self.validar(value)==0:
            try:
                os.remove("/home/pi/webapp/static/themes/images/clothes/" + str(value) +".jpg")
                print("true")
            except:
                print("false")
                pass
	
	
    def validar(self, slot):
	archivo = "/home/pi/webapp/static/themes/images/clothes/"+ str(slot) +".jpg"
	try:
    	    with open(archivo, 'r') as file:
        	file = file.read()
		return 0
	except:
	    pass
    	    return 1