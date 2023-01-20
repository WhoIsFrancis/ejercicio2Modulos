import time

tiempo_actual = time.strftime("%H:%M", time.localtime())
hora = int(time.strftime("%H"))
minutos = int(time.strftime("%M"))
semana_laboral = (1 <= int(time.strftime("%w", time.localtime())) >= 5)

if hora >= 19 and semana_laboral:
    print("Es hora de ir a casa, son las ", tiempo_actual)
else:
    print("Quedan", (18 - hora), "y ", (59 - minutos), "minutos para que termine la jornada laboral")
