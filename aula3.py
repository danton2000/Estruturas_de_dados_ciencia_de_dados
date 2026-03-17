"""
Solicite ao usuário 3 notas da prova 1 e 3 notas da prova 2.
Exiba a média do estudante

Utilize somente numpy e operações basicas para tal.

Colocar a lista num array

lista array + lista array / 2
"""
import numpy as np # type: ignore

lista_prova1 = []
lista_prova2 = []

loop = 3

while True:

    if loop == 0:
        break

    nota = int(input("Digite nota da prova 1: "))
    # Armazenando os valores em uma lista
    lista_prova1.append(nota)

    nota = int(input("Digite nota da prova 2: "))
    # Armazenando os valores em uma lista
    lista_prova2.append(nota)

    loop -= 1

# Forma mais complexa
# jogando os valores de uma lista em um array
array_provas = np.array(lista_prova1 + lista_prova2)

print(array_provas)

array_provas = array_provas.reshape(2,3)

print(array_provas)

print(np.mean(array_provas, axis=0))


# forma simples
# array_prova1 = np.array(lista_prova1)

# array_prova2 = np.array(lista_prova2)

# # Calculando os arrays
# soma = array_prova1 + array_prova2

# print(soma)

# media = soma / 2

# print(media)