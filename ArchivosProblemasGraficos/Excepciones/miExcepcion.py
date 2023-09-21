#Creando mi propia excepcion personalizada
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f'Impresionante, cometiste el siguiente error: {err}')

# #Lanzando mi propia excepcion
# raise MiExcepcion('JAJAJAJ, persona poco culta')

#Manejandola
try:
    raise MiExcepcion('JAJAJAJ, persona poco culta')
except:
    print('Como vas a cometer ese error?')
    