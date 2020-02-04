for i in range(1, 101):  # loop de 1 a 100
    if i%3 == 0 and i%5 == 0:  # si es multiplo de 3 y 5
        print('FizzBuzz', end=', ')  # 'end' para imprimir con comas
        continue  # salta al prox numero
    elif i%3 == 0:  # si es multiplo de 3
        print('Fizz', end=', ')
    elif i%5 == 0:  # si es multiplo de 5
        print('Buzz',  end=', ')
    else:  # si no es multiplo de 3 o 5
        print(i, end=', ')