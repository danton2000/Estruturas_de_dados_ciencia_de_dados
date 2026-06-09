from ListaEncadeada import ListaEncadeada

lista = ListaEncadeada()

lista.append("Danton")

lista.append("Maria")

lista.append("Luana")

print(lista)

print(len(lista))

print(lista[0])

lista[2] = "Daniel"

print(lista[0])

print(lista)

lista.remove("Maria")

print(lista)

lista.append("Cristino Ronaldo")

print(lista)

lista.remove("Danton")

print(lista)