import math
varhyppt = float(input("ingrese distancia respecto al objetivo en km "))
varcatetopuesto = float(input("ingrese altura del objetivo en km "))
velocidad = float(input("ingrese velocidad en km/s "))
var = (300000)
#aqui comienza las operaciones
hyp = float((2*varhyppt)/(var))
grados = (math.asin(varcatetopuesto/varhyppt))
gradosr = float(math.degrees(grados))
#aqui terminan las operaciones
#aqui empieza a imprimir.
print(".......................................")
print(f"la onda tardó en regresar {hyp} segundos")
print (f"el angulo con el que fue lanzada la onda fue de {gradosr} grados")
