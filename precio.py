#Meterle un descuento a un precio y que devuelva el precio rebajado
precio=input("Precio original: " )
descuento=input("Descuento aplicado: ")

pfinal = float(precio) - (float(precio) * float(descuento)/100)

print (f"El precio final del producto es {pfinal}")