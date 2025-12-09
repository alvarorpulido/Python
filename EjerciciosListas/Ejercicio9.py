palabra = input("Introduce una palabra: ").lower()
vocales = "aeiou"
for vocal in vocales:
    print(f"{vocal}: {palabra.count(vocal)}")