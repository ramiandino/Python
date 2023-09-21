# 2 listas,una con nombres y otra con apellidos.
nombres = ["Ramiro","Dana"]
apellidos = ["Andino","Sorokoswki"]

#Registrar esta informacion en un TXT de forma optima.

with open("ArchivosProblemasResueltos\\nombresYapellidos.txt","w") as arch:
    arch.writelines("Los datos son:\n\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n--------\n") for n,a in zip(nombres,apellidos)]


#Esto funciona igual.  
# for n,a in zip(nombres,apellidos):
#     arch.writelines(f"Nombre: {n}\nApellido: {a}\n--------\n")
    