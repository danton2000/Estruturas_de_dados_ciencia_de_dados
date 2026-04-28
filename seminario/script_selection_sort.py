def selection_sort(lista):
    # tamanho da lista
    n = len(lista)

    #print(f"Tamanho lista: {n}")

    # laço de repetição, vai rodar 5x
    for i in range(n):
        menor_indice = i
        print(f"Menor indice: {menor_indice}")

        # laço de repetição i+1, 5
        # avança uma casa
        for j in range(i+1, n):
            print(f"Valor de I: {i}")
            print(f"Valor de J: {j}")
  
            if lista[j] < lista[menor_indice]:
                print(f"{lista[j]} menor {lista[menor_indice]}")
                menor_indice = j
                print(f"menor_indice: {menor_indice}")

        # troca dos numeros da lista       
        lista[i], lista[menor_indice] = lista[menor_indice], lista[i]
        print(f"Lista alterada: {lista}")   

if __name__ == "__main__":
    lista = [5, 3, 8, 1, 2]

    print("Lista Desordenada.")
    print(lista)

    selection_sort(lista)
    # print("Lista Ordenada.")
    # print(lista)