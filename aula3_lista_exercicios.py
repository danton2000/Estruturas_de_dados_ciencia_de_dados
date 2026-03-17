"""
Dada a matriz de notas ao lado, considere que
cada linha é um aluno e cada coluna é uma prova:
1. mostrar a nota do 3° aluno na 2a prova
2. calcular a média de cada aluno
3. calcular a média de cada prova
4. descobrir a maior nota da matriz
5. adicionar 0.5 ponto a todas as notas
"""

import numpy as np # type: ignore

notas = np.array ([
    #nota1, nota2, nota3
    [7.0, 8.5, 6.0], #aluno1
    [9.0, 7.5, 8.0], #aluno2
    [5.5, 6.5, 7.0], #aluno3
    [8.0, 9.0, 9.5]  #aluno4
])

#1. mostrar a nota do 3° aluno na 2a prova

print("mostrar o elemento da linha 3, coluna 2")
print(notas[2, 1])

# 2. calcular a média de cada aluno
# axis = 1, é a linha do array que representa os alunos
print(np.mean(notas, axis=1))

#3. calcular a média de cada prova
print(np.mean(notas, axis=0))

#4. descobrir a maior nota da matriz
print(np.max(notas))

#5. adicionar 0.5 ponto a todas as notas
print(notas + 0.5)

####

# Lista de Exercícios
# Manipulação de Dados com a Biblioteca NumPy
# Importante:
# Certifique-se de ter o NumPy instalado (pip install numpy).
# Inicie seus scripts com import numpy as np.

# 1. Criando arrays básicos

# Crie, com NumPy:
# a) um array com os valores 5, 10, 15, 20
array_a = np.array ([
    
    [5, 10, 15, 20]
])

# b) uma matriz 2x3 com valores definidos por você
matrix_b = np.array([

    [0,1,2],
    [0,1,2]
])


# c) uma matriz 3x4 preenchida com zeros
matrix_c = np.array([

    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
])

# d) uma matriz 2x5 preenchida com uns
matrix_d = np.array([

    [0,0,0,0,0],
    [0,0,0,0,0]
])

# 2. Investigando um array
# Crie a matriz abaixo:
# [[2, 4, 6],
#  [8, 10, 12]]
# Mostre: o número de dimensões, o formato da matriz, a quantidade total de elementos e o tipo dos dados armazenados.

matrix = np.array([

    [2, 4, 6],
    [8, 10, 12]
])

print("número de dimensões")
print(matrix.shape)

print("formato da matriz")
print(matrix)

print("quantidade total de elementos")
print(matrix.size)

print("tipo dos dados armazenados")
print(matrix.dtype)

# 3. Sequência e reorganização
# Use np.arange() para criar um array com os números de 1 até 12. Depois:
# a) reorganize em uma matriz 3x4
# b) reorganize em uma matriz 4x3
# c) explique por que não seria possível reorganizar esse mesmo array em uma matriz 5x3

# Criando array com os valores de 1 até 12
array = np.arange(1,13)

print(array)

print("a) reorganize em uma matriz 3x4")
array = array.reshape(3,4)
print(array)

print("b) reorganize em uma matriz 4x3")
array = array.reshape(4,3)
print(array)

print("c) explique por que não seria possível reorganizar esse mesmo array em uma matriz 5x3")
print("Pelo o que eu pude entender, não a elemente suficente para organizar os valores na estrutura desejada 5x3")

# 4. Acessando elementos e fatias
# Considere a matriz:
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]
# Mostre: o primeiro elemento, o elemento central, o último elemento, a segunda linha inteira, a terceira coluna inteira e a submatriz formada pelas 2 primeiras linhas e 2 últimas colunas.

matrix = np.array([

    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("o primeiro elemento")

print(matrix[0,0])

print("o elemento central")
print(matrix[1,1])

print("o último elemento")
print(matrix[-1,-1])

print("a segunda linha inteira")
print(matrix[1])

print("a terceira coluna inteira")
print(matrix[:, -1:])

print("a submatriz formada pelas 2 primeiras linhas")

print("e 2 últimas colunas")