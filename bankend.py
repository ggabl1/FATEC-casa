senhaCorreta = int(input('defina a senha'))
senha = int(input('Digite a senha'))
for senhaErrada in range(0, 6):
    if senha != senhaCorreta and senhaErrada <= 4:
        print('Senha inválida')
        senha = int(input('Digite a senha novamente'))
    elif senhaErrada >= 5:
        print('Número de tentativas esgotado')
        break
    else:
        print('Loguin realizado com sucesso')
        break