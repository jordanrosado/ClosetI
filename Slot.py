import mysql.connector

class piSlot(object):
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

