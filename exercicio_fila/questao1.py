"""
Questão 1 — Fila de atendimento de chamados
Uma central de suporte recebe chamados de alunos com dúvidas sobre atividades. 
Os chamados devem ser atendidos na ordem em que chegam, ou seja, o primeiro chamado registrado deve ser o primeiro a ser atendido.

Crie um programa em Python usando deque que permita:
adicionar um chamado à fila;
atender o próximo chamado da fila;
visualizar qual é o próximo chamado sem removê-lo;
exibir todos os chamados pendentes;
encerrar o programa.

Cada chamado pode ser representado apenas pelo nome do aluno ou por uma breve descrição, como:
"Ana - dúvida no exercício 3"

O programa deve usar um menu com while e if/elif/else.
Exemplo de menu esperado:
    1 - Adicionar chamado
    2 - Atender próximo chamado
    3 - Ver próximo chamado
    4 - Exibir fila
    5 - Sair
    
Requisito importante:
Use append() para adicionar chamados ao fim da fila e popleft() para atender o chamado que está na frente.
"""

from collections import deque

fila = deque()

# Adicionando elementos na fila, sempre no final.
def enqueue(fila, valor):
    """Enfileira `valor` no fim da lista `fila`."""
    fila.append(valor)

# Removendo elementos da fila, sempre do inicio.
def dequeue(fila):
    """Desenfileira o primeiro elemento da lista `fila`."""
    if len(fila) > 0:
        return fila.pop()
    
# Mostrando o primeiro elemento da fila, sem remover.
def front(fila):
    """Retorna o primeiro elemento da lista `fila`."""
    if len(fila) > 0:
        return fila[0]

# Mostrando o tamanho da fila.
def size(fila):
    """Retorna o tamanho da lista `fila`."""
    return len(fila)

while True:

    print("1 - Adicionar chamado")
    print("2 - Atender próximo chamado")
    print("3 - Ver próximo chamado")
    print("4 - Exibir fila")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    # Implementação das opções do menu

    # Adicionar chamado
    if opcao == "1":
        chamado = input("Digite o chamado (ex: 'Ana - dúvida no exercício 3'): ")
        enqueue(fila, chamado)
        print("Chamado adicionado à fila.")

    # Atender próximo chamado (remover o primeiro da fila)
    elif opcao == "2":
        if size(fila) > 0:
            atendido = dequeue(fila)
            print(f"Chamado atendido: {atendido}")
        else:
            print("Não há chamados para atender.")

    # Ver próximo chamado (mostrar o primeiro da fila sem remover)
    elif opcao == "3":
        if size(fila) > 0:
            proximo = front(fila)
            print(f"Próximo chamado: {proximo}")
        else:
            print("Não há chamados na fila.")

    # Exibir fila (mostrar todos os chamados pendentes)
    elif opcao == "4":
        if size(fila) > 0:
            print("Chamados pendentes:")
            for chamado in fila:
                print(chamado)
        else:
            print("Não há chamados na fila.")

    # Encerrar o programa
    elif opcao == "5":
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")