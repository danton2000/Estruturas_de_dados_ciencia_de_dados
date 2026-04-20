# Lista de exercícios

# Questão 1
def primeiro( lista):
    return lista[0]
# Responda:
# Qual é a complexidade?

#Resposta: A complexidade é O(1) porque acessar o primeiro item de uma lista é sempre rápido, não importa o tamanho da lista.

# Questão 2
def soma_total( lista):
     soma = 0
     i = 0

     while i < len( lista):
         soma += lista[ i]
         i += 1

     return soma
# Responda:
# Qual é a complexidade?

# Resposta: A complexidade é O(n) porque o programa precisa passar por todos os itens da lista, um por um, para somá-los. Quanto maior a lista, mais tempo ele leva.

# Questão 3
def ordena_e_mostra( lista):
     nova = sorted( lista)
     return nova[ 0]
# Responda:
# Qual é a complexidade da função sorted()?
# Resposta: A complexidade da função sorted() é O(n log n), porque ela utiliza algoritmos eficientes de ordenação, como o Timsort.

# Qual é a complexidade total da função ordena_e_mostra?
# Resposta: A complexidade total da função ordena_e_mostra(lista) é O(n log n), já que o tempo para acessar o primeiro elemento da lista ordenada é O(1) e não afeta o tempo total.

# Contagem regressiva
# Escreva uma função recursiva chamada contagem_regressiva(n) que exiba os números de n até 0.

# Exemplo:
# contagem_regressiva( 4)

# Saída esperada:
# 4
# 3
# 2
# 1
# 0

def contagem_regressiva(n):
    if n < 0:
        return
    print(n)
    contagem_regressiva(n - 1)

contagem_regressiva(4)

# Soma de 1 até n
# Escreva uma função recursiva chamada soma_ate_n(n) que retorne a soma de todos os números de 1 até n.

# Exemplo:
# print( soma_ate_n( 5))

# Saída esperada:
# 15

def soma_ate_n(n):
    if n <= 0:
        return 0
    return n + soma_ate_n(n - 1)

print(soma_ate_n(5))

# Soma dos elementos de uma lista
# Escreva uma função recursiva chamada soma_lista(lista, n) que some os n primeiros elementos de uma lista.

# Exemplo:
# print( soma_lista([ 3, 5, 2, 4], 4))

# Saída esperada:
# 14

def soma_lista(lista, n):
    if n <= 0:
        return 0
    return lista[n - 1] + soma_lista(lista, n - 1)

print(soma_lista([3, 5, 2, 4], 4))

# Inverter string
# Escreva uma função recursiva chamada inverte_texto(texto) que retorne a string invertida.

# Exemplo:
# print( inverte_texto( "python"))

# Saída esperada:
# nohtyp

def inverte_texto(texto):
    if len(texto) == 0:
        return ""
    return texto[-1] + inverte_texto(texto[:-1])

print(inverte_texto("python"))

# Verificar palíndromo
# Escreva uma função recursiva chamada eh_palindromo(texto) que retorne True se a palavra for um palíndromo e False caso contrário.

# Exemplo:
# print( eh_palindromo( "arara"))
# print( eh_palindromo( "python"))

# Saída esperada:
# True
# False

def eh_palindromo(texto):
    if len(texto) <= 1:
        return True
    if texto[0] != texto[-1]:
        return False
    return eh_palindromo(texto[1:-1])

print(eh_palindromo("arara"))
print(eh_palindromo("python"))

# Pilha da soma
# Analise a função abaixo e escreva a pilha de execução para a chamada soma_ate_n(4).
def soma_ate_n( n):
     if n == 1:
         return 1
     else:
         return n + soma_ate_n( n - 1)

# Resposta:
# soma_ate_n(4) -> 4 + soma_ate_n(3)
# soma_ate_n(3) -> 3 + soma_ate_n(2)
# soma_ate_n(2) -> 2 + soma_ate_n(1)
# soma_ate_n(1) -> 1 (caso base)

# Encontrando o erro lógico
# O código abaixo tenta calcular o fatorial, mas está incorreto. Explique o erro.

def fatorial( n):
     if n == 0:
         return 0
     else:
         return n * fatorial( n - 1)
     
#Explique:
# por que ele está errado;
# Resposta: O erro está no caso base. O fatorial de 0 é 1, não 0. A função deve retornar 1 quando n for 0 para calcular o fatorial corretamente.

# qual deveria ser o caso base correto.
def fatorial( n):
     if n == 0:
         return 1
     else:
         return n * fatorial( n - 1)
     
# Comparando funções
# Observe as duas funções:
def funcao_a( n):
     if n == 0:
         return 0
     else:
         return 1 + funcao_a( n - 1)

def funcao_b( n):
     if n == 0:
         return 1
     else:
         return n * funcao_b( n - 1)
# Responda:
# o que a funcao_a calcula?
# Resposta: A função funcao_a conta até chegar no número n. Para cada chamada, ela soma 1 até chegar no caso base, que é 0. Por exemplo, se n = 5, ela retorna 5.

# o que a funcao_b calcula?
# Resposta: A função funcao_b calcula o fatorial de n. Ela multiplica n pelos números anteriores até chegar no caso base, que é 1. Por exemplo, se n = 5, ela retorna 120.

# qual a diferença entre os casos base das duas?
# Resposta: O caso base da funcao_a retorna 0, porque ela está contando as chamadas recursivas. Já o caso base da funcao_b retorna 1, porque ela está multiplicando os números para calcular o fatorial.