from colorthief import ColorThief
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

color_thief = ColorThief('/home/pi/webapp/clothes/2.jpg')
# build a color palette
palette = color_thief.get_palette(color_count=6)
print palette
#print palette
