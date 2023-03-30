carros = ["Voyagem", "Gol", "GTR", "Bwm", "McLaren", "Hilux", "Citroen", "Porshe"]
print(carros[0])


for x in carros:
    print(x) 
    if x == "Bwm":
        print("  -I8")
    if x == "Hilux":
        break

print("")

for y in "Alfabeto":
    print(y)