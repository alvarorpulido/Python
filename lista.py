lista = [1,2,3,4,5,6]
print(lista)
lista.append(4) #Inserta al final de la lista
print(lista)
lista.insert(1,100) #Inserta en una posicion específica
print(lista)
lista.pop() #Elimina el último elemento de la lista
print(lista) 
lista.sort(reverse=True) #La muestra al reves
print(lista)
print(lista.count(3)) #Cuenta cuantas veces aparece algo en la lista
print(max(lista)) #Muestra el numero mas grande
print(min(lista)) #Muestra el numero mas pequeño
print(sum(lista)) #Muestra la suma de la lista
print(len(lista)) #Muestra la longitud de la lista


meses = {1:'enero',2:'febrero'} #Lista que asigna los numeros al valor en la lista
print(meses[1])

profes = {'sri':'fernando','iaw':'nuria','sad':'miguel angel'}
profes['aso']='javier' #Agregacion de elemento a la lista anterior
print(profes['sri'])
print(profes['aso'])
modulo = input('Introduce el modulo: ')
profe = input('Introduce el profe: ')
profes[modulo] = profe #Agregar a la lista el el elemento y la asignacion solicitados anteriormente en input
print(profes)


diccionario = {'table':'mesa','orange':'naranja','red':'rojo'}
print(diccionario['orange'])