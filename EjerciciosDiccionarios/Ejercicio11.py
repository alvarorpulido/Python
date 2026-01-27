texto = """nif;nombre;email;teléfono;descuento
01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5
71476342J;Macarena Ramírez;macarena@mail.com;692839321;8
63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2
98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"""

lineas = texto.split('\n')
campos = lineas[0].split(';')

clientes = {}

for linea in lineas[1:]:
    datos = linea.split(';')
    nif = datos[0]
    clientes[nif] = {
        'nombre': datos[1],
        'email': datos[2],
        'teléfono': datos[3],
        'descuento': float(datos[4])
    }

print(clientes)
