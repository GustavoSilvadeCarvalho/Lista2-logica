compra1 = float(input("Digite o valor da primeira compra: "))
compra2 = float(input("Digite o valor da segunda compra: "))
compra3 = float(input("Digite o valor da terceira compra: "))

total = compra1 + compra2 + compra3

if total > 300:
    desconto = total * 0.2
elif total > 200:
    desconto = total * 0.15
elif total > 100:
    desconto = total * 0.1
else:
    desconto = 0

total_com_desconto = total - desconto

print(f"Valor total das compras: R$ {total:.2f}")
print(f"Desconto concedido: R$ {desconto:.2f}")
print(f"Valor total com desconto: R$ {total_com_desconto:.2f}")
print("Gustavo Silva de Carvalho")
print("RA:105139241103")
print("Caio Henrique Ferreira de Souza")
print("RA:1051392411028")