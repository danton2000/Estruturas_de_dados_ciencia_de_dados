# 1. Cadastro de Convidados
# Crie um programa que peça ao utilizador o nome de 3 convidados através do input(). Armazene-os numa lista e depois:
# Ações: Adicione um 4º convidado chamado "Penetra", imprima o tamanho da lista (len) e remova o segundo convidado.

#Crie um programa que peça ao utilizador o nome de 3 convidados através do input()
lista_convidados = []

loop = 3

while True:

    if loop == 0:
        break

    convidado = input("Nome do convidado: ")
    # Armazene-os numa lista e depois
    lista_convidados.append(convidado)

    loop -= 1
# Adicione um 4º convidado chamado "Penetra"
convidado = "Penetra"

# Armazene-os numa lista
lista_convidados.append(convidado)

print(lista_convidados)

len(lista_convidados)

# remova o segundo convidado.
lista_convidados.pop(1)

print(lista_convidados)

# 2. Manipulação Numérica
# Crie uma lista com os números de 10 a 100 (incrementando de 10 em 10). Utilize fatiamento para criar uma nova lista apenas com os valores de 30 a 60 e, em seguida, inverta a ordem da lista original usando reverse().
# Exemplo: Após inverter, imprima os dois últimos elementos usando índices negativos.

# Criar uma lista
lista_numeros = []

# Incrementar valores na lista de 10 em 10, até 100
for numeros in range(0, 110, 10):
    
    lista_numeros.append(numeros)

# Fatiando os valores(30 a 60), e criando uma nova lista
lista_numeros_fatiado = lista_numeros[3:7]
print(lista_numeros_fatiado)

#inverta a ordem da lista original usando reverse().
lista_numeros.reverse()
print(lista_numeros)

#Após inverter, imprima os dois últimos elementos usando índices negativos.
print(lista_numeros[-2:])

# 3. Fila de Banco
# Simule uma fila de espera. Adicione "Ana", "Carlos" e "Beto" à lista. Remova a primeira pessoa da fila utilizando pop() no índice correto e exiba quem está a ser atendido.
# Dica: Verifique em que posição o cliente "Beto" ficou após o atendimento da primeira pessoa.

# Adicione "Ana", "Carlos" e "Beto" à lista
lista_espera = ["Ana", "Carlos", "Beto"]

# Remova a primeira pessoa da fila utilizando pop() no índice correto
lista_espera.pop(0)

# exiba quem está a ser atendido
print(lista_espera)

# Beto ficou no indice 1, antes ele era o 2.

# 5. O Desafio do Inversor 
# Peça ao utilizador para digitar uma frase qualquer, palavra por palavra, e armazene as palavras numa lista. Utilize o truque do fatiamento com passo negativo para exibir a frase invertida. Desafio: pesquise sobre o método split em python e tente usar.
# Exemplo: Entrada "Python é legal" -> Saída "legal é Python".

lista_frases = []

# Peça ao utilizador para digitar uma frase qualquer

frase = input("Digite uma frase: ")
# palavra por palavra, e armazene as palavras numa lista
lista_frases.append(frase)

# Utilize o truque do fatiamento com passo negativo para exibir a frase invertida
frase = frase.split()

print(frase[::-1])

# 6. Integrador: Sistema de Notas
# Receba 4 notas de um aluno, ordene-as da maior para a menor, remova a menor nota da lista e calcule a média aritmética das notas restantes.
# Fórmulas: Use sum() para somar e len() para contar os elementos no cálculo da média.

lista_notas = []

loop = 4

while True:

    if loop == 0:
        break
    # Receba 4 notas de um aluno    
    nota = int(input("Digite a nota: "))
    # Armazene-os numa lista e depois
    lista_notas.append(nota)

    loop -= 1

# ordene-as da maior para a menor
lista_notas.sort(reverse=True)

print(lista_notas)

# remova a menor nota da lista e calcule
lista_notas.pop(-1)
print(lista_notas)

# calcule a média aritmética das notas restantes.
media = sum(lista_notas) / len(lista_notas)

print(media)