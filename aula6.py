# Qual complexidade desse algoritmo

array = [1,2,3] # Array de validação
n = 3 # n = numero de elementos do array

def tem_duplicacao(array, n):
    i = 0 # 1 execução

    while i < n: # n + 1 execuções
        val = array[i] # n execuções
        j = i + 1 # n execuções

        while j < n: # n + 1 execuções
            if array[j] == val: # n execuções
                return True # n execuções
            j += 1 # n execuções

        i += 1 # n execuções

    return False # 1 execução

# t(n) = 4 + 8n

# Eliminando as constantes

# t(n) = n

# 0(n), complexidade linear

# Resposta certa nxn... wtf... 

def ache_min(array, n):
    minimo = array[0] # 1 execução
    i = 0 # 1 execução

    while i < n: # n + 1 execuções
        if array[i] < minimo: # n execuções
            minimo = array[i] # n execuções
        i += 1 # n execuções

    return minimo # 1 execução

# t(n) = 4 + 4n

# Eliminando as constantes

# t(n) = n

# 0(n), complexidade linear 

def remover(lista, i):
    lista.pop(i)

# O(n)

# Negocio bem desgraçado ein kk