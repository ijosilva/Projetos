import os


carros = []
carro = input("Digite o nome do carro ou 0 para sair: ")

while carro != "0":
    carros.append(carro)
    carro = input("Digite o nom do carro ou 0 para sair: ")


os.system('clear')

for x in carros:
    print(x)


print("\nFim do programa")

print("\n")
