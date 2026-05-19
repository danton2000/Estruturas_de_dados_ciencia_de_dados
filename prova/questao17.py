def conta_positiva(lista, n):

    quantidade = 0 # 1

    for i in range(n):

        if lista[i] > 0: # n + 1

            quantidade = quantidade + 1 # n

    return quantidade # 1

# t(n) = 3 + 2n

# t(n) = n

lista_a = [1,2,3]

lista_b = [4,5,6]

print(f"Saida: {conta_positiva(lista_a, len(lista_a))}")

print("Complexidade: Será a O(n), que representa a complexidade linear, linear por que a ideia do algorimo é percorrer os elementos de uma lista")