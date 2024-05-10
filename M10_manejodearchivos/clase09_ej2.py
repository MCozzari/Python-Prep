import sys

if len(sys.argv)==4:
    import os
    import datetime

    marcadetiempo=datetime.datetime.now()
    marcadetiempo=int(datetime.datetime.timestamp(marcadetiempo))

    temperatura=sys.argv[1]
    humedad=sys.argv[2]
    llovio=sys.argv[3]
    linea=(str(marcadetiempo) + ", temperatura: "+ temperatura + ". humedad: "+ humedad + ". llovio? "+llovio)


    logs_lluvia=open("clase09_ej2.csv","a")
    logs_lluvia.write(linea +"\n")
    logs_lluvia.close()
else:
    print("No se han detectado 3 elementos, porfavor asegurese de introducirlos")
    print("Ejemplo: clase09_ej2.py <temperatura> <humedad> <llovio>")