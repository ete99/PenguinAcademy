from random import randint

def juego(end = 100):  
    ''' El juego '''
    print(f'El rango es de 1 a {end}.')
    numero_secreto = randint(1, end)
    fin = False
    prueba = -1
    numero_intentos = 0
    while not fin:
        print('Adivina el numero:')
        try:
            prueba = int(input())  # Lee la cantidad de usd a cambiar
        except:
            print('***Inserte solo numeros***')  # si no inserto un numero
        finally:
            numero_intentos += 1
            if prueba == numero_secreto:
                print('¡Felicidades! Lo has adivinado')
                print(f'Te tomaron {numero_intentos} intentos')
                fin = True
            elif prueba < numero_secreto:
                print('Lo siento, ¡inténtalo dSe nuevo! Muy bajo.')
            else:
                print('Lo siento, ¡inténtalo de nuevo! Muy alto.')

try:
    print('Inserte el maximo de rango(Enter = 100):')
    end = int(input())
    juego(end)  # Si elige un rango especifico
except:
    juego() # El default 100

