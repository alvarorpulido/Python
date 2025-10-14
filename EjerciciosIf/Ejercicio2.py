pssw = str(input("Contraseña: "))
real_pssw = "User123*"
if pssw.upper() == real_pssw.upper():
    print ("Contraseña correcta")
else:
    print ("Contraseña incorrecta")