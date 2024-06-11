feminino = 0
masculino = 0
avaliacaoPositiva = 0
avaliacaoNegativa = 0
porcentagem = 0
quantidadeDeEntrevistados = int(input("quantas pessoas serao entrevistadas? "))
for i in range (quantidadeDeEntrevistados):
    sexo = str(input("Digite seu sexo (responda com f ou m): "))
    if sexo == "f":
        feminino += 1
    elif sexo == "m":
        masculino += 1

    avaliacao = str(input("O produto atendeu suas necessidades com qualidade? (responda com s ou n): "))
    if avaliacao == "s":
        avaliacaoPositiva += 1
    elif avaliacao == "n":
        avaliacaoNegativa += 1

    if sexo == "f" and avaliacao == "s":
        porcentagemf = ((feminino / quantidadeDeEntrevistados)*100)
    if sexo == "m" and avaliacao == "n":
        porcentagemm = ((masculino / quantidadeDeEntrevistados)*100)

print("a) Avaliações Positivas:", avaliacaoPositiva)
print("b) Avaliações Negativas:", avaliacaoNegativa)
print("c) Porcentagem de mulheres com avaliações positivas:", porcentagemf, "%")
print("d) Porcentagem de homens com avaliações negativas:", porcentagemm, "%")