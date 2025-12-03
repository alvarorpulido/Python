abecedario = list("abcdefghijklmnñopqrstuvwxyz")
resultado = [letra for i, letra in enumerate(abecedario, start=1) if i % 3 != 0]
print(resultado)
