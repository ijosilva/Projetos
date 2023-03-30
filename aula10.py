a = int(input("A - Digite um numero: "))
b = int(input("B - Digite um numero: "))
res = 0

if a>b:
    print("A > B")
    res = a + b
    print("A operacao: " + str(a) + " + " + str(b) + " = "+ str(res))

elif a<b:
    print("A > B")
    res = a - b
    print("A operacao: " + str(a) + " - " + str(b) + " = "+ str(res))

elif (a==b):
    print("A > B")
    res = a - b
    print("A operacao: " + str(a) + " - " + str(b) + " = "+ str(res))

else:  
    print("Operacao invalida!")

print("==========Fim do programa==========")