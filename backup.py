import datetime       # importar modulo del tiempo
import os      # importar modulo de sistema operativo
import shutil  # importar modulo de administracion de archivos

dt = datetime.datetime.now() # creacion de variable dt para definir fecha de archivos
 
nombre = "Copia de seguridad creada el dia {} del mes {} del año {}  a las {} horas con {} minutos y {} segundos ".format(dt.day, dt.month, dt.year, dt.hour, dt.minute, dt.second) # parametros del archivo

shutil.make_archive(nombre, "zip", "carpeta_anadir_archivos") # crear archivo compreso 

inicio = [] #inicializar lista de archivos
total = os.listdir()

for a in total:
    if a.startswith("Copia de seguridad creada el dia") == True:
        inicio.append(a)

rutadestino = "/Users/edgardmendoza/Desktop/prueba/" #Ruta de destino externa

for i in inicio:
    shutil.move(i, rutadestino) # mover archivo ala ruta de destino