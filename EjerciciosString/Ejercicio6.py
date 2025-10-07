frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal: ").lower()
frase_modificada = ""
for char in frase:
    if char.lower() == vocal:
        frase_modificada += char.upper()
    else:
        frase_modificada += char
print(f"Frase con la vocal '{vocal}' en mayúscula: {frase_modificada}")