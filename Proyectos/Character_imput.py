from datetime import date
from datetime import datetime
fecha_actual = datetime.now ()

print (" Bienvenido a su calculadora para saber cuando cumplira 100 años ")
name = input (" Por favor digame su Nombre ")
if name.isalpha ():
    edad = input (" ¿Cuantos años tiene? ")
    if  edad.isdigit ():
        edad_100 = (fecha_actual.year - edad) + 100
        print (f" Usted {name} cumplira 100 años en el el año {edad_100}")
    else:
        raise ValueError ("Por favor digite su edad en forma numerica")
else: 
    raise ValueError ("Ese no es un nombre valido ")



