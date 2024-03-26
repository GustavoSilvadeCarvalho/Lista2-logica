altura = float(input("Digite a altura em metros: "))
sexo = input("Digite o sexo (masculino/feminino): ")

def calcular_peso(altura, sexo):
    if sexo.lower() == 'masculino':
        peso_ideal = (72.7 * altura) - 58
    elif sexo.lower() == 'feminino':
        peso_ideal = (62.1 * altura) - 44.7
    else:
        print("Por favor, insira 'masculino' ou 'feminino' como sexo.")
        return None
    return peso_ideal

peso_ideal = calcular_peso(altura, sexo)
if peso_ideal is not None:
    print("O peso ideal é: {:.2f} kg".format(peso_ideal))

print("Gustavo Silva de Carvalho")
print("RA:105139241103")
print("Caio Henrique Ferreira de Souza")
print("RA:1051392411028")