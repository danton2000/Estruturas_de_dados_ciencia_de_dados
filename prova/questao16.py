def busca_binaria(lista, valor):

    print(f"Lista inicial {lista}")

    inicio = 0

    fim = len(lista) - 1

    i = 1

    while inicio <= fim:

        print(f"Iteração numero {i}")

        meio = (inicio + fim) // 2

        print(f"Indice do Meio da lista {meio}")

        if lista[meio] == valor:

            print(f"Valor {valor} Localizado")
            return True
        
        elif valor < lista[meio]:

            fim = meio - 1

            print(f"Indice do Fim da lista {fim}")

        else:
            inicio = meio + 1

            print(f"Indice do Inicio da lista {inicio}")
        
        i += 1

    print("-1 Valor não localizado")
    return False

lista = [2,5,8,12,16,21,30,37,45]

busca_binaria(lista, 21)

busca_binaria(lista, 100)