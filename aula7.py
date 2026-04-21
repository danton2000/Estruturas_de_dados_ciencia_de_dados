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

    inicio = 0

    fim = len(lista_numeros) - 1

    while inicio <= fim:

        meio = (inicio + fim) // 2

        #print(lista_numeros[meio])

        if lista_numeros[meio] == numero:

            return True
        
        elif numero < lista_numeros[meio]:

            fim = meio - 1

        else:
            inicio = meio + 1
    
    return False

print(busca_numeros_binarias(10))