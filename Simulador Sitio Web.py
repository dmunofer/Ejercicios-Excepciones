import re


correo=input('Introduzca su correo electrónico')

if re.search(". * @. * \ .. *", correo):


elif correo =='':
    raise Exception('Es un una entrada incorrecta. Introduzca una dirección válida')

elif len(correo)==5:
    raise Exception('')
else:
    raise Exception('Una dirección de correo debe tener el formato xxx@xxx.xx')