print("Ingrese tamano de memoria");
tamMemoria=int(input())
print("Ingrese cantidad de particiones");
cantParticiones=int(input())

sistOp=tamMemoria//10
idParticionActual=1
posicionActualMemoria=sistOp
#Crear memoria vacia
memoria=[]
tablaParticiones=[]
tablaProcesos=[]
i = 0

def bestFit(tabla,sizeProceso):
    mejorparticion=10000 #MaxValue
    for i in tabla:
        if i[3] == False:
            if (i[2]-i[1]) > sizeProceso and i[2]-i[1] < mejorparticion:
                mejorparticion=i[0]
    if mejorparticion==10000:
        return False
    else:
        tabla[mejorparticion][3]=True
        tabla[mejorparticion][4]= len(tablaProcesos)
        tablaProcesos.append([tabla[mejorparticion][4],mejorparticion])
        return True

def imprimeTabla(tabla):
    print("Tabla de Particiones")
    print("ID    Inicio    Fin    Estado     Proceso")
    print("-------------------------------------")
    for i in tabla:
        print(i)
    print("----------------------------------------")
def imprimememoria(mem):
    print("Memoria")
    print("-------------------------------")
    print(mem)
    print("-------------------------------")
          
for i in range(0,sistOp):
        memoria.append("S")
for i in range(sistOp,tamMemoria):
    memoria.append("_")
imprimememoria(memoria)

tamanoRestanteMemoria=tamMemoria-sistOp
continuar = True
while continuar and cantParticiones > 0:
    print("Desea crear otra particion? Y/N")
    decision=input()
    if decision == "Y":
        print("Ingresar tamano de particion")
        tamanoNuevaParticion=int(input())
        if tamanoNuevaParticion <= (tamanoRestanteMemoria-cantParticiones) and tamanoNuevaParticion > 0:#esto se asegura de dejar aunque sea un byte para cada particion restante.
            tablaParticiones.append([idParticionActual,posicionActualMemoria,posicionActualMemoria+tamanoNuevaParticion,False,-1])
            for i in range(posicionActualMemoria,posicionActualMemoria+tamanoNuevaParticion):
                memoria[i]=idParticionActual
            posicionActualMemoria+=tamanoNuevaParticion
            cantParticiones-=1
            idParticionActual+=1
            
        else:
            if tamanoNuevaParticion > (tamanoRestanteMemoria-cantParticiones):
                print("Particion muy grande. Error")
            else:
                print("Particion demasiado pequena")
            
    else:
        continuar=False
    imprimememoria(memoria)
    imprimeTabla(tablaParticiones)


continuar = True

while continuar == True:
    print("Ingresar Tamaño proceso")
    nuevoProcesoTamano=int(input())
    if bestFit(tablaParticiones,nuevoProcesoTamano) == True:
        print("Proceso insertado con exito")
    else:
        print("No Hay espacio. Compactando")
        compactar()
        if bestFit(tablaParticiones,nuevoProcesoTamano) == True:
            print("Proceso insertado con exito")
        else:
            print("No hay espacio. Imposible insertar")
    imprimememoria(memoria)
    imprimeTabla(tablaParticiones)
    print("Desea agregar otro proceso?")
    if input()!="y":
        continuar = False