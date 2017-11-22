import time
import subprocess 
from flask import *
from Camera import piCamera
from Slot import piSlot	
from Clasificador import piClasificador

cam = piCamera()
slot = piSlot()
clas = piClasificador()

app = Flask(__name__)

@app.route("/")
def main():
	    return render_template('pagina.html')

@app.route("/camera", methods=['POST'])
def camera():	
	   #subprocess.call(['python','/home/pi/webapp/motorFoto.py'])
	   #time.sleep(3)
	   slotdis = slot.encontrar_slot()
           #Codigo para mover a posicion de toma de foto
           #cam.take(3)
	   clas.agregar(slotdis, cam.take(slotdis))
	   #subprocess.call(['python','/home/pi/webapp/moverRiel.py'])
	   #subprocess.call(['python','/home/pi/webapp/motorSlot.py',format(slotdis)])
	   #Codigo servomotor y motor DC
	   #subprocess.call(['python','/home/pi/webapp/servo.py'])
	   #time.sleep(3)
	   #subprocess.call(['python','/home/pi/webapp/motorRegresar.py',format(slotdis)])	
	   return 'OK'
	   

@app.route("/dispensar/<int:slo>", methods=['POST'])
def dispensar(slo):
	   #Codigo para sacar ropa
	   cam.delete(slo) 
	   clas.eliminar_slot(slo)	
	   print("Eliminar")
	   return 'OK'
	   #Codigo para mover a posicion del slot

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)