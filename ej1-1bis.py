import sys #Necesario para el exit

""" Yo entendi el enunciado diferente a Ale, para mi dice que hay que poner un tamaño de memoria y dsepues (restando la 
memoria para el SO) dividir en patriciones fijas (pero pueden ser de diferentes tamaños).
 El codigo hasta el primer while es igual al de Ale"""
 
print("Ingrese tamano de memoria");
tamMemoria=int(input())
print("Ingrese cantidad de particiones");
cantParticiones=int(input())
if cantParticiones >= tamMemoria:
	print(">>> Cantidad de memoria superada <<<")
	print(">>> Se ingreso mas particiones que memoria disponible <<<")
	sys.exit(1)
cantParticiones += 1 # < -- Esto aca puse por que me toma 1 particion menos de la que ingreso, no se en que parte le erre
					 		# despues veo el codigo a ver si encuentro el error o si alguien quiere verlo seria genial
sistOp=tamMemoria//10
cantParticiones-=1 #Considerando que el espacio de sistema es una particion tambien
idParticionActual=1
posicionActualMemoria=sistOp
#Crear memoria vacia
memoria=[]
tablaParticiones=[]
i = 0

def imprimeTabla(tabla):
    print("Tabla de Particiones")
    print("ID    Inicio    Fin")
    print("-------------------------------------")
    print(tabla)
    print("----------------------------------------")
def imprimememoria(mem):
    print("Memoria")
    print("-------------------------------")
    print(mem)
    print("-------------------------------")

for i in range(0,sistOp):
        memoria.append(0)
for i in range(sistOp,tamMemoria):
    memoria.append("_")
imprimememoria(memoria)

while cantParticiones > 0:
	if (tamMemoria - posicionActualMemoria) == cantParticiones: #Se hace esto para que cada particion tenga por lo menos 1 Byte
																#por ej, si hay 3 particiones mas y solo 3 posiciones de memoria entra aca y hace el bucle
		print(" >>> La cantidad de particiones es igual a la memoria restante <<<") # <-- esto se podria que borrar obviamente xd
		tamParticion = 1
		while cantParticiones > 0:
			tablaParticiones.append([idParticionActual,posicionActualMemoria,posicionActualMemoria + tamParticion]) 
			for i in range(posicionActualMemoria,posicionActualMemoria+tamParticion): #para cargar la lista memoria (igual al de ale)
				memoria[i]=idParticionActual
			cantParticiones -= 1
			posicionActualMemoria = posicionActualMemoria + tamParticion #actualizamos la posicion de memoria actual
			idParticionActual += 1
	else:
		print("Ingrese el tamaño de la particion ",idParticionActual)
		print(" EL tamaño maximo a ingresar es: ", (tamMemoria - posicionActualMemoria)-cantParticiones + 1)
		tamParticion = int(input())
		if tamParticion > ((tamMemoria - posicionActualMemoria) - cantParticiones + 1):  #si superamos la memoria disponible sale por exit
			print(">>> Cantidad de memoria superada <<<")
			sys.exit(1)
		else:
			tablaParticiones.append([idParticionActual,posicionActualMemoria,posicionActualMemoria + tamParticion])
			for i in range(posicionActualMemoria,posicionActualMemoria+tamParticion):
				memoria[i]=idParticionActual
			cantParticiones -= 1
			posicionActualMemoria = posicionActualMemoria + tamParticion
			idParticionActual += 1


imprimememoria(memoria)
imprimeTabla(tablaParticiones)
