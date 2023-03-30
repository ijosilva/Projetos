# -*- coding: utf-8 -*-
list = ["item0", "item1", "item2"]

print(list)

print("O item dois da lista é:")
print(list[2])

print("Adicionando itens na lista, temos:")
list.append("item3")

print(list)


print("O numero de itens na lista é:")
print(str(len(list)) + " itens na lista")


print("Removendo itens da lista: ")
list.remove(list[0])
print(list)
