num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

#somar
def soma(a, b):
    return a + b

#subtrair
def subtracao(a, b):
    return a - b

#multiplicar
def multiplicacao(a, b):
    return a * b

#dividir
def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero!"

print("Soma:", soma(num1, num2))
print("Subtração:", subtracao(num1, num2))
print("Multiplicação:", multiplicacao(num1, num2))
print("Divisão:", divisao(num1, num2))
print("Gustavo Silva de Carvalho")
print("RA:105139241103")
print("Caio Henrique Ferreira de Souza")
print("RA:1051392411028")