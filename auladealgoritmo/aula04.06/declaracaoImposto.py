continua = True
while (continua):
    nome = str(input("digite o seu nome "))
    cpf = int(input("digite o seu cpf "))
    RA = float(input("digite a sua renda anual "))
    dependentes = int(input("digite o numero de dependentes "))
    aliquota = 0
    desconto = dependentes * 200
    RL = RA - desconto
    if (RL <= 1900):
        aliquota = None
    elif(RL <= 7000 and RL >= 1901):
        aliquota = 5
    elif(RL >= 7001 and RL <= 15000):
        aliquota = 15
    elif(RL >= 15001):
        aliquota = 27
    pergunta = str(input("deseja continuar? (s/n)"))
    if (pergunta == "s"):
        continua = True
    else:
        continua = False
        break
print(nome, cpf, "renda anual: ", RA, "numero de dependentes: ", dependentes, "aliquota: ", aliquota,"%")