import re

text = "The quick brown fox jumped over the lazy dog"

x = re.search("^The.*dog$", text)

if x:
    print("SI")
else:
    print("NO")
    
#Expresion regular validada.