#cambios, precios basados en maxicambios 25/01/2020
cant_cambiar = -1
prec_compra_usd = 6250

while cant_cambiar < 0:  # sigue el loop hasta que inserte el input correcto
    print('Inserte la cantidad de dolares que desea cambiar a guaranies: ')
    try:
        cant_cambiar = float(input())  # Lee la cantidad de usd a cambiar
    except:
        print('\033[H\033[J')  # Limpia la pantalla
        print('***Inserte solo numeros***')
print(f'{cant_cambiar}$ equivale a aprox. Gs{cant_cambiar*prec_compra_usd}')
