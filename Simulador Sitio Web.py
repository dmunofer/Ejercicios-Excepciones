import re


correo=input('Introduzca su correo electrónico')

if re.search(". * @. * \ .. *", correo):
    cadenas = correo.split('@')
    cadena_final = '¡Bienvenido '+ cadenas[0] +'!'
    print(cadena_final)


elif correo =='':
    raise Exception('Es un una entrada incorrecta. Introduzca una dirección válida')

elif len(correo)==5:
    raise Exception('Cuenta bloqueada a causa de un ataque')
else:
    raise Exception('Una dirección de correo debe tener el formato xxx@xxx.xx')