lista_numeros = [0,1,2]

# Busca linear
def encontre_numero_lista(numero):

    for i in lista_numeros:
        print(i)

        if i == numero:
            return True
    
    return False

# Complexidade desse codigo é n?
# Pior das hipoteses 0(n)
# A melhor é 1(n)

#print(encontre_numero_lista(3))

def encontre_numero_lista_recursiva(numero):
    
    print(lista_numeros)

    if lista_numeros == numero:
        return True

    lista_numeros[-1] + encontre_numero_lista(numero - 1)
    

print(encontre_numero_lista_recursiva(1))

# Busca Binaria

# achar numero 21

lista_numeros = [2,5,8,12,16,21,30,37,45]

# olhar o elemento do meio
# 16

# indice da metade
indice_metade = len(lista_numeros) // 2

#print(lista_numeros[indice_metade:])

# print(lista_numeros[:indice_metade])

def encontre_numero_lista(numero):

    # Verificando se o numero é menor que o numero da metade da lista
    if numero < lista_numeros[indice_metade]:
        # percorrendo na metade da lista que tem os menores numeros
        for i in lista_numeros[:indice_metade]:
            #print(lista_numeros[indice_metade])

            if i == numero:
                return True
            else:
                return False
    else:
        # percorrendo na metade da lista que tem os maiores numeros
        for i in lista_numeros[indice_metade:]:
            #print(lista_numeros[indice_metade])

            if i == numero:
                return True
            else:
                return False
    
    
print(encontre_numero_lista(21))

def busca_numeros_binarias(numero):
    """
    Realiza uma busca binária em uma lista ordenada para verificar se um número está presente.

    A busca binária é um algoritmo eficiente para encontrar um elemento em uma lista ordenada.
    O algoritmo divide a lista em duas partes a cada iteração, reduzindo o espaço de busca pela metade.

    Parâmetros:
    ----------
    numero : int
        O número que será procurado na lista.

    Retorno:
    --------
    bool
        Retorna True se o número for encontrado na lista, caso contrário, retorna False.

    Complexidade:
    -------------
    - Melhor caso: O(1), quando o número está no meio da lista.
    - Pior caso: O(log n), onde n é o tamanho da lista.

    Exemplo de uso:
    ---------------
    lista_numeros = [2, 5, 8, 12, 16, 21, 30, 37, 45]
    print(busca_numeros_binarias(2))  # Saída: True
    print(busca_numeros_binarias(50))  # Saída: False
    """

    inicio = 0  # Índice inicial da lista
    fim = len(lista_numeros) - 1  # Índice final da lista

    while inicio <= fim:  # Enquanto houver elementos na lista para verificar
        meio = (inicio + fim) // 2  # Calcula o índice do meio da lista

        # Verifica se o número no meio é o número procurado
        if lista_numeros[meio] == numero:
            return True
        
        # Se o número procurado for menor, ajusta o índice final
        elif numero < lista_numeros[meio]:
            fim = meio - 1

        # Se o número procurado for maior, ajusta o índice inicial
        else:
            inicio = meio + 1
    
    # Retorna False se o número não for encontrado
    return False

# Exemplo de chamada da função
print(busca_numeros_binarias(2))  # Saída: True