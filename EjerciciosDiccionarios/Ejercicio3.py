frutas={
    "platano":1.35,
    "manzana":0.80,
    "pera":0.85,
    "naranja":0.70    
}
nFruta=input("¿Qué fruta quieres?: ")
nKilos=int(input("¿Cuántos kilos quieres?: "))

if nFruta in frutas:
    print(f"El total son {nKilos*frutas[nFruta]} €")
else:
    print("Lo siento, esa fruta no está disponible")