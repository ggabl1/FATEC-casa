while True:
    idade = int(input("digite sua idade "))
    if idade < 18:
        print("menor de idade")
    elif idade < 65:
        print("maior de idade")
    else:
        print("maior de 65 anos")