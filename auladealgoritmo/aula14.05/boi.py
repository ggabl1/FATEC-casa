bois = []
def cadastrarBoi():
    numeroBois = int(input("digite a quantidade de bois "))
    for i in range (1,numeroBois+1):
        boi = {
            "id": i,
            "peso": float(input('digite o peso do boi {i}'))
        }
        bois.append(boi)
def boiMaisPesado():
    maiorPeso = 0
    for boi in bois:
        if boi["peso"] > maiorPeso:
            maiorPeso = boi["peso"]
    for boi in bois:
        if boi["peso"] == maiorPeso:
            return print ("boi mais pesado: {boi}")
def boiMaisLeve():
    menorPeso = 10000
    for boi in bois:
        if boi["peso"] < menorPeso:
            menorPeso = boi["peso"]
    for boi in bois:
        if boi["peso"] == menorPeso:
            return print("boi mais leve: {boi}")
                
cadastrarBoi()
boiMaisPesado()
boiMaisLeve()