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
    return False

lista = [2,5,8,12,16,21,30,37,45]

busca_binaria(lista, 8)

# Lista inicial [2, 5, 8, 12, 16, 21, 30, 37, 45]
# Iteração numero 1
#     Indice do Meio da lista 4
#     Indice do Fim da lista 3
# Iteração numero 2
#     Indice do Meio da lista 1
#     Indice do Inicio da lista 2
# Iteração numero 3 - Ultima
#     Indice do Meio da lista 2
#     Valor 8 Localizado