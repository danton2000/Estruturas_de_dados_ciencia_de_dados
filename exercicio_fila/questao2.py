"""
Questão 2 — Simulador de fila de atendimento com prioridade simples
Uma central de atendimento acadêmico recebe solicitações de estudantes. Cada solicitação possui um nome e um tipo.
O tipo da solicitação pode ser:
normal
urgente

Crie um programa em Python que simule o atendimento usando duas filas:
fila_urgente
fila_normal

Regras do sistema:
- solicitações urgentes entram na fila_urgente;
- solicitações normais entram na fila_normal;
- ao atender, o sistema deve verificar primeiro se há alguém na fila urgente;
- se houver solicitação urgente, ela deve ser atendida antes das normais;
- se não houver ninguém na fila urgente, o sistema atende a fila normal;
- dentro de cada fila, a ordem deve continuar sendo FIFO;
- o sistema deve permitir cadastrar solicitações, atender a próxima, listar pendentes e encerrar.

Use deque, append() e popleft().
Exemplo de estrutura esperada:
from collections import deque

fila_urgente = deque()
fila_normal = deque()

Exemplo de menu esperado:
1 - Cadastrar solicitação
2 - Atender próxima solicitação
3 - Listar solicitações pendentes
4 - Exibir quantidade de pendentes
5 - Sair

Desafio adicional:
Ao listar as solicitações pendentes, exiba separadamente:
solicitações urgentes;
solicitações normais;
quantidade de solicitações em cada fila.

Importante:
Mesmo que a fila urgente tenha prioridade, a ordem dentro dela também deve respeitar FIFO. Ou seja, entre as solicitações urgentes, a primeira urgente cadastrada deve ser a primeira urgente atendida.
"""

from collections import deque

fila_urgente = deque()
fila_normal = deque()

def cadastrar_solicitacao():
    nome = input("Digite o nome do estudante: ")
    tipo = input("Digite o tipo da solicitação (normal/urgente): ").strip().lower()
    
    if tipo == "urgente":
        fila_urgente.append(nome)
        print(f"Solicitação urgente de {nome} cadastrada.")
    elif tipo == "normal":
        fila_normal.append(nome)
        print(f"Solicitação normal de {nome} cadastrada.")
    else:
        print("Tipo de solicitação inválido. Use 'normal' ou 'urgente'.")

def atender_proxima_solicitacao():
    if fila_urgente:
        atendida = fila_urgente.popleft()
        print(f"Atendendo solicitação urgente de {atendida}.")
    elif fila_normal:
        atendida = fila_normal.popleft()
        print(f"Atendendo solicitação normal de {atendida}.")
    else:
        print("Não há solicitações para atender.")

def listar_solicitacoes_pendentes():
    print("Solicitações urgentes pendentes:")
    for solicitacao in fila_urgente:
        print(f"- {solicitacao}")
    
    print("\nSolicitações normais pendentes:")
    for solicitacao in fila_normal:
        print(f"- {solicitacao}")
    
    print(f"\nQuantidade de solicitações urgentes: {len(fila_urgente)}")
    print(f"Quantidade de solicitações normais: {len(fila_normal)}")

while True:
    print("\n1 - Cadastrar solicitação")
    print("2 - Atender próxima solicitação")
    print("3 - Listar solicitações pendentes")
    print("4 - Exibir quantidade de pendentes")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_solicitacao()
    elif opcao == "2":
        atender_proxima_solicitacao()
    elif opcao == "3":
        listar_solicitacoes_pendentes()
    elif opcao == "4":
        print(f"Quantidade de solicitações urgentes: {len(fila_urgente)}")
        print(f"Quantidade de solicitações normais: {len(fila_normal)}")
    elif opcao == "5":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")