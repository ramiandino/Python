import re

text = "Reemplazando todas las vocales por asteriscos"

new_text = re.sub("[aeiou]", "*", text)  #Cada una por separado va a encontrar al ponerle el array.

print(new_text)  