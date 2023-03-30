clima = "sol"
money = 500
lugar = ""

if clima =="sol" or (100 <= money <= 600):
    lugar = "Piscina"

else:
    lugar = "Ski"

print("Vou para a(o) " + lugar)


#AND
# V V = V
# V F = F
# F V = F
# F F = F

#OR
# V V = V
# V F = V
# F V = V
# F F = F