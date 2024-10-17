#Variable del diccionario
print(" ")
print("pr_3_2do_Variable_Diccionario_Mendez_Sanchez_Maria_Guadalupe_Yazmin__3w_1199")
print(" ")
divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}      #Definir la variable
print(divisas)                                          #Imprimir la varaible
print(" ")
opcion = str(input("¿Qué divisa deseas poner?: \n"))    #Imprimir la divisa que deseas poner
opcion = opcion.title()                                 #Convierte la respuesta en mayuscula
print(" ")
if opcion in divisas:                                   #ve la opcion en las divisas
    print(divisas[opcion])                              #Verificar si se encuentra en la variable
else:
    print("No se encuentra la divisa en el diccionario") #Imprime no se encuentra la divisa en diccionario
print(" ")
