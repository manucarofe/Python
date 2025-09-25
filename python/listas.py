### Listas ###

mi_lista = list()
mi_lista_ordenada = []
## Una lista se puede declarar de estas dos formas ##

mi_lista = [21, 1.72, "Manuel", "Fernandez"]
print(mi_lista)
print(len(mi_lista)) #"Len" se utiliza para saber tamaño de la lista
print(type(mi_lista)) #"type" se utiliza para saber de que tipo es


mi_lista_ordenada = [20, 20, 18, 84, 53, 21]
print(mi_lista_ordenada)
print(len(mi_lista_ordenada))
print(type(mi_lista_ordenada))

print(mi_lista_ordenada[-1]) #Imprime el ultimo elemento de la lista
print(mi_lista[0]) #Primer elemento de la lista
print(mi_lista[2]) #Tercer elemento de la lista
print(mi_lista[3]) #Cuarto elemento de la lista
print(mi_lista_ordenada.count(20)) #Lo que hace "Conut" es retornar el numero de ocurrencias de un valor

#print(mi_lista[-5]) #IndexError : Está fuera del rango
#print(mi_lista[-6]) #IndexError : Está Fuera del rango


edad, altura, nombre, apellido = mi_lista #A sto se le llama desempaquetado, estamos dershaciendo la lista
print(edad)


print(mi_lista + mi_lista_ordenada) #Esto lo que hace es unir las listas


mi_lista.append("Manucarofe") #Se usa para añadir datos a la lista
print(mi_lista)

mi_lista.insert(2, "SevillaFC") #Inserta el dato que quieras en la posición que le asignes
print(mi_lista)

mi_lista.remove("SevillaFC") #Elimina el dato que sabes que esta en la lista
print(mi_lista)

print(mi_lista_ordenada)
mi_lista_ordenada.pop()
print(mi_lista_ordenada.pop())
print(mi_lista_ordenada)
# El pop, si no le asignamos una posición, elimina el último elemento de la lista #


mi_elememto_pop = mi_lista_ordenada.pop(1)
print(mi_elememto_pop)
print(mi_lista_ordenada)
## El pop consiste en eliminar un elemento de la lista pero lo retorna y podemos almacenarlo en una variable ##


del mi_lista_ordenada[2] 
print(mi_lista_ordenada)
#El "del" se diferencia del remove porque elimina el elemento que esta en la posición dada

mi_nueva_lista = mi_lista_ordenada.copy()

#"Clear" borra todo el contenido de la lista
mi_lista_ordenada.clear()
print(mi_lista_ordenada)
print(mi_nueva_lista)

mi_nueva_lista.reverse() #Le da la vuelta al orden los elementos de la lista
print(mi_nueva_lista)

mi_nueva_lista.sort()
print(mi_nueva_lista)


mi_lista = "Soy el mejor delegado"
print(mi_lista)
print(type(mi_lista))
#Con esto lo que hemos hecho es basicamente cambiar la lista "mi_lista" a un string