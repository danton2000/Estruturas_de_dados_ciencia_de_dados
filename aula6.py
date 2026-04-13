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

# Análise da Complexidade
# 1. Laço Externo (while i < n)
# O laço externo é controlado pela variável i, que vai de 0 até n-1.
# Ele executa n vezes no pior caso.
# 2. Laço Interno (while j < n)
# Para cada valor de i, o laço interno é controlado pela variável j, que começa em i + 1 e vai até n-1.
# O número de iterações do laço interno depende do valor de i:
# Quando i = 0, o laço interno executa n - 1 vezes.
# Quando i = 1, o laço interno executa n - 2 vezes.
# ...
# Quando i = n - 1, o laço interno executa 0 vezes.
# 3. Soma Total de Iterações
# O número total de iterações do laço interno é:
# [
# (n - 1) + (n - 2) + (n - 3) + \dots + 1 + 0
# ]

# Essa soma é uma progressão aritmética com (n) termos, onde o primeiro termo é (n - 1) e o último termo é (0). A soma é dada por:
# [
# \text{Soma} = \frac{n \cdot (n - 1)}{2}
# ]

# Portanto, o número total de passos do algoritmo é proporcional a (n^2).

def ache_min(array, n):
    minimo = array[0] # 1 execução
    i = 0 # 1 execução

    while i < n: # n + 1 execuções
        if array[i] < minimo: # n execuções
            minimo = array[i] # n execuções
        i += 1 # n execuções

    return minimo # 1 execução

# Análise da Complexidade
# 1. Operações fora do laço
# As linhas minimo = array[0] e i = 0 são executadas uma vez cada. Isso é O(1).
# 2. Laço while i < n
# O laço while roda n vezes no pior caso, pois i vai de 0 até n-1.
# Dentro do laço:
# A comparação if array[i] < minimo é executada n vezes.
# A atribuição minimo = array[i] é executada no máximo n vezes (no caso em que cada elemento é menor que o anterior).
# O incremento i += 1 é executado n vezes.
# 3. Operação após o laço
# A linha return minimo é executada uma vez. Isso é O(1).
# Complexidade Total
# O número total de passos é proporcional ao número de iterações do laço, que é n.
# Ignorando constantes e termos menores, a complexidade de tempo é O(n) (tempo linear).
# Complexidade de Espaço
# O algoritmo usa apenas variáveis auxiliares (minimo e i), independentemente do tamanho da entrada.
# Portanto, a complexidade de espaço é O(1) (constante).
# Resumo
# Complexidade de Tempo: O(n) (linear).
# Complexidade de Espaço: O(1) (constante).
# Se precisar de mais explicações, é só avisar!

def remover(lista, i):
    lista.pop(i)

# Análise da Complexidade
# 1. Operação pop(i)
# A função pop(i) remove o elemento no índice i da lista.
# Se o índice i for o último elemento da lista, a operação é O(1) (tempo constante), pois não há necessidade de deslocar elementos.
# No entanto, se o índice i estiver no início ou no meio da lista, todos os elementos após o índice precisam ser deslocados uma posição para a esquerda.
# No pior caso (removendo o primeiro elemento), todos os elementos da lista são deslocados, o que resulta em O(n), onde n é o tamanho da lista.
# Complexidade Total
# Complexidade de Tempo: O(n) no pior caso, devido ao deslocamento dos elementos.
# Complexidade de Espaço: O(1), pois a operação é feita diretamente na lista e não utiliza memória adicional significativa.
# Resumo
# Complexidade de Tempo: O(n) (linear).
# Complexidade de Espaço: O(1) (constante).
# Se precisar de mais explicações ou exemplos, é só avisar!