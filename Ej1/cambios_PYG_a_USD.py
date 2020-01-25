#cambios, precios basados en maxicambios 25/01/2020
cant_cambiar = -1
prec_venta_usd = 6350

while cant_cambiar < 0:   # sigue el loop hasta que inserte el input correcto
    print('Inserte la cantidad de guaranies que desea cambiar a dolares: ')
    try:
        cant_cambiar = float(input())  # Lee la cantidad de usd a cambiar
    except:
        print('\033[H\033[J')  # Limpia la pantalla
        print('***Inserte solo numeros***')
print(f'Gs{cant_cambiar} equivale a aprox. {cant_cambiar/prec_venta_usd}$')