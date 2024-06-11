valorDiaria = 0
nome = str(input("digite seu nome "))
TipoAp = str(input("digite tipo do apartamento hospedado "))
numDiarias = int(input("digite o numero de diarias utilizadas "))
CI = float(input("digite o valor do consumo interno "))
if (TipoAp == "A"):
    valorDiaria = 250
elif (TipoAp == "B"):
    valorDiaria = 150
elif (TipoAp == "C"):
    valorDiaria = 100
elif (TipoAp == "D"):
    valorDiaria = 75
totalDiarias = numDiarias * valorDiaria
subtotal = totalDiarias + CI
taxaServico = subtotal/10
totalGeral = subtotal + taxaServico
print("total das diarias R$", totalDiarias, ", subtotal R$", subtotal, ", taxa de serviço R$", taxaServico, ", total geral R$", totalGeral)