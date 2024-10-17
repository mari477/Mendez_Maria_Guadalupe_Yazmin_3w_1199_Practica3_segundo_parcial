#Precios
print(" ")
print("pr_3_2do_Presios_Mendez_Sanchez_Maria_Guadalupe_Yazmin__3w_1199")
print(" ")
frutas = {"platano":"30", "manzana":"20", "pera":"28", "naranja":"40",}       #Definir mi variable
print (frutas)                                                                #Imprimir la variable
opc = str(input("¿Que fruta deseas comprar?\n"))                              #Imprimir que fruta deseas comprar
print(" ")
opc = opc.lower()                                                             #Convierte en minusculas
if opc in frutas:                                         
    kilos = float(input("¿cuantos kilos deseas llevar?\n"))                   #Definir kilos
    print(" ")
    precio = kilos*(float(frutas[opc]))                                       #Hacer la operacion del precio para convertir
    print("El precio es:$"+str(precio))                                       #Imprimir el precio
    print(" ")
else:
    print("Lo sentimos esta fruta no esta en el intinerario")                 #Imprimir que no esta en intinerario
print(" ")