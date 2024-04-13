numeroCerto = int(input('escreva um numero de 1 a 10: '))
contador = 1
tentativa = 0
if numeroCerto <= 10 and numeroCerto >= 1:
    while tentativa != numeroCerto:
        tentativa = int(input('escreva um numero de 1 a 10: '))
    if contador >= 1 and tentativa != numeroCerto:
        print('voce errou')
        contador+1
    elif tentativa == numeroCerto:
        print('voce acertou')