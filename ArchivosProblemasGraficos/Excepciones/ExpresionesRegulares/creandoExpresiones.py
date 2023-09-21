import re
#Detectando un numero CABA y ocultandolo.

text = "Hola Ramiro, mi numero es: +54 9 221 507-5454"

pattern = r'\+\d{2}\s\d{1}\s\d{3}\s\d{3}-\d{4}'

reemplazo = re.sub(pattern,"(Numero oculto)",text)  

print(reemplazo)