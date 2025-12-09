numeros = input("Introduce números separados por comas: ")
lista = [float(n) for n in numeros.split(",")]
media = 0
for x in lista:
    media += x
media = media / len(lista)
varianza = 0
for x in lista:
    varianza += (x - media) ** 2
varianza = varianza / len(lista)
desviacion = varianza ** 0.5
print("Media:", media)
print("Desviación típica:", desviacion)