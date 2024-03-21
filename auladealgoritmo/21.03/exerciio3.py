km = float(input('escreva a quantidade de quilometros rodados: '))
consumo = float(input('escreva o consumo total: '))
resultado = km/consumo
print ('o resultado é: ', resultado)
if resultado <= 8:
    print('o automóvel está consumindo muito combustível')
else:
    print('o consumo está bom')
    