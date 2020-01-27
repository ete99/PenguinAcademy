def desplazar(pal, desp):
    return pal[desp:]+pal[:desp]

arr = ['oscreem', 'ueq', 'la', 'óncodificaci', 'ñaense', 'eshabilidad', 'eld', 'losig', '21', 'osusam', 'la', 'óncodificaci', 'moco', 'nau', 'taherramien', 'rapa', 'armostr', 'moco']

new_arr=[]
for i in arr:
    new_arr.append(desplazar(i, 2))
print(new_arr)

resultado=''
for i in new_arr:
    resultado = resultado + ' ' + i
#print(resultado)  # para dejar en una oracion