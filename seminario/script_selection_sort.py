def selection_sort(lista):
    # Calcula o tamanho da lista
    n = len(lista)

    # Laço externo: percorre cada elemento da lista
    for i in range(n):
        # Define o índice do menor elemento como o índice atual
        menor_indice = i
        print(f"Menor indice: {menor_indice}")

        # Laço interno: percorre os elementos restantes da lista (à direita de i)
        for j in range(i+1, n):
            print(f"Valor de I: {i}")  # Mostra o índice atual do laço externo
            print(f"Valor de J: {j}")  # Mostra o índice atual do laço interno
  
            # Verifica se o elemento atual (lista[j]) é menor que o elemento no menor_indice
            if lista[j] < lista[menor_indice]:
                print(f"{lista[j]} menor {lista[menor_indice]}")  # Mostra a comparação
                menor_indice = j  # Atualiza o índice do menor elemento
                print(f"menor_indice: {menor_indice}")  # Mostra o novo menor índice

        # Troca os elementos: coloca o menor elemento encontrado na posição correta
        lista[i], lista[menor_indice] = lista[menor_indice], lista[i]
        print(f"Lista alterada: {lista}")  # Mostra o estado da lista após a troca

# Bloco principal do programa
if __name__ == "__main__":
    # Define uma lista de números desordenados
    lista = [5, 3, 8, 1, 2]

    # Exibe a lista desordenada
    print("Lista Desordenada.")
    print(lista)

    # Chama a função de ordenação
    selection_sort(lista)

    # Exibe a lista ordenada (comentado no código original)
    # print("Lista Ordenada.")
    # print(lista)