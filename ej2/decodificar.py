def desplazar(pal, desp):
    return pal[desp:]+pal[:desp]  # decodifica

arr = ['oscreem', 'ueq', 'la', 'óncodificaci', 'ñaense', 'eshabilidad', 'eld', 'losig', '21', 'osusam', 'la', 'óncodificaci', 'moco', 'nau', 'taherramien', 'rapa', 'armostr', 'moco']

new_arr=[]
for i in arr:
    new_arr.append(desplazar(i, 2))  # desplaza y adhiere al nuevo array
print(new_arr)  # imprime el array

resultado=''
for i in new_arr:
    resultado = resultado + ' ' + i
#print(resultado)  # imprime el resultado en una oracion en una oracion