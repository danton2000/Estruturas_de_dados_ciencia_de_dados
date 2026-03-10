import numpy as np # type: ignore

# Pratica 1
dados = np.array(
    [
        [5,8,2],
        [1,7,9]
    ]
)

# Estrutura - shape
print(dados.shape)

# Qtd de elementos
print(dados.size)

# Pratica 2
matriz = np.array(

    [
        [3,6,9],
        [2,4,8],
        [1,5,7]
    ]

)

print(matriz)

print("mostrar o elemento da linha 2, coluna 1")
print(matriz[2, 1])

print("mostrar a segunda linha")
print(matriz[1])

print("mostrar a terceira coluna")
print(matriz[0:3, 2])