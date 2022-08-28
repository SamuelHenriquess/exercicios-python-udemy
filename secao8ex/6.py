def convert(hora, minuto, seg):
    horaseg = hora * 3600
    minutoseg = minuto * 60
    print(horaseg, minutoseg, seg)

horas = int(input('digite o valor das horas: '))
minutos = int(input('digite o valor dos minutos: '))
segs = int(input('digite o valor dos segundos: '))

convert(horas,minutos,segs)