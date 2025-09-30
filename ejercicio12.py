x = 3.49
d = 0.60
br = int(input("Número de barras de pan no frescas vendidas: "))
desc = x * d
p = x - desc
c = p * br
print(f"Precio habitual de una barra: {x} €")
print(f"Descuento por no ser fresca: {desc} €")
print(f"Coste final total: {c} €")
