from ArvoreBinariaBusca import ArvoreBinariaBusca

# Exercícios de prática

# Desenvolva as soluções usando a classe de BST trabalhada em aula. Sempre que um método for recursivo, prefira separar um método público de um método auxiliar iniciado por `_`.

## Exercício 1 — Busca booleana

# Implemente o método `contains(value)`, que deve retornar:

# - `True`, quando o valor existir na árvore;
# - `False`, quando o valor não existir.

# Exemplo:

# ```python
# bst.contains(30)   # True
# bst.contains(999)  # False
# ```

# Não utilize listas nem os percursos da árvore para resolver.
arvore = ArvoreBinariaBusca()
arvore.insert(30)
arvore.insert(10)
arvore.insert(50)

print(arvore.contains(30))   # True
print(arvore.contains(999))  # False

## Exercício 2 — Soma dos valores

# Implemente o método `sum_values()`, que devolve a soma de todos os valores armazenados na árvore.

# Exemplo:

# ```
#        10
#       /  \
#      5    15

# sum_values() -> 30

arvore = ArvoreBinariaBusca()
arvore.insert(10)
arvore.insert(5)
arvore.insert(15)

print(arvore.sum_values())  # 30

## Exercício 3 — Soma apenas dos valores pares

# Implemente `sum_even_values()`, que retorna somente a soma dos nós cujo valor é par.

# Exemplo:

# ```
#        10
#       /  \
#      5    14
#     /      \
#    2        17

# sum_even_values() -> 26

arvore = ArvoreBinariaBusca()
arvore.insert(10)
arvore.insert(5)
arvore.insert(14)
arvore.insert(2)
arvore.insert(17)

print(arvore.sum_even_values())  # 26

## Exercício 4 — Remover o menor valor

# Implemente `remove_min()`, que remove o menor valor da árvore e retorna esse valor. Caso a árvore esteja vazia, retorne `None`.

# Dica: o menor valor é o nó mais à esquerda; depois de encontrá-lo, reaproveite a ideia dos casos de remoção.

arvore = ArvoreBinariaBusca()
arvore.insert(20)
arvore.insert(10)
arvore.insert(30)
arvore.insert(5)

print(arvore.remove_min())  # 5

## Exercício 5 — Verificar se a árvore está balanceada

# Crie o método `is_balanced()`.

# Para este exercício, considere uma árvore balanceada quando, em todos os nós, a diferença entre a contagem dos nos da subárvore esquerda e os nos da subárvore direita for no máximo `1`.

arvore = ArvoreBinariaBusca()
arvore.insert(10)
arvore.insert(5)
arvore.insert(15)
arvore.insert(2)

print(arvore.is_balanced())  # True

## Exercício 6 — Aplicação com menu

# Crie um programa de terminal que use uma BST para armazenar números inteiros. O menu deve permitir:

# ```
# 1 - Inserir valor
# 2 - Buscar valor
# 3 - Remover valor
# 4 - Exibir valores em ordem
# 5 - Exibir valores em pré-ordem
# 6 - Exibir valores em pós-ordem
# 7 - Mostrar menor e maior valor
# 8 - Mostrar quantidade de nós, folhas e altura
# 9 - Sair
# ```

# Requisitos:

# - informe claramente quando uma inserção não ocorrer por valor repetido;
# - informe quando a busca encontrar ou não encontrar o valor;
# - informe quando uma remoção for bem-sucedida ou quando o valor não existir;
# - mantenha o menu em repetição até a pessoa escolher sair;
# - use métodos da classe para realizar as operações, sem colocar toda a lógica diretamente no `while` do menu.

def mostrar_menu():
    print("\n=== Menu da BST ===")
    print("1 - Inserir valor")
    print("2 - Buscar valor")
    print("3 - Remover valor")
    print("4 - Exibir valores em ordem")
    print("5 - Exibir valores em pré-ordem")
    print("6 - Exibir valores em pós-ordem")
    print("7 - Mostrar menor e maior valor")
    print("8 - Mostrar quantidade de nós, folhas e altura")
    print("9 - Sair")


def inserir_valor(arvore):
    try:
        valor = int(input("Digite o valor a ser inserido: "))
    except ValueError:
        print("Valor inválido. Digite um número inteiro.")
        return

    if arvore.insert(valor):
        print(f"Valor {valor} inserido com sucesso.")
    else:
        print(f"O valor {valor} já existe na árvore. Inserção não realizada.")


def buscar_valor(arvore):
    try:
        valor = int(input("Digite o valor a ser buscado: "))
    except ValueError:
        print("Valor inválido. Digite um número inteiro.")
        return

    if arvore.contains(valor):
        print(f"Valor {valor} encontrado na árvore.")
    else:
        print(f"Valor {valor} não encontrado na árvore.")


def remover_valor(arvore):
    try:
        valor = int(input("Digite o valor a ser removido: "))
    except ValueError:
        print("Valor inválido. Digite um número inteiro.")
        return

    if arvore.remove(valor):
        print(f"Valor {valor} removido com sucesso.")
    else:
        print(f"Valor {valor} não existe na árvore. Remoção não realizada.")


def exibir_em_ordem(arvore):
    print("Valores em ordem:", arvore.em_order())


def exibir_pre_ordem(arvore):
    print("Valores em pré-ordem:", arvore.pre_order())


def exibir_pos_ordem(arvore):
    print("Valores em pós-ordem:", arvore.pos_order())


def mostrar_min_max(arvore):
    menor = arvore.minimo()
    maior = arvore.maximo()

    if menor is None or maior is None:
        print("A árvore está vazia.")
    else:
        print(f"Menor valor: {menor}")
        print(f"Maior valor: {maior}")


def mostrar_resumo(arvore):
    if arvore.is_empty():
        print("A árvore está vazia.")
        return

    print(f"Quantidade de nós: {arvore.contar_nos()}")
    print(f"Quantidade de folhas: {arvore.contar_folhas()}")
    print(f"Altura da árvore: {arvore.altura()}")


def main():
    arvore = ArvoreBinariaBusca()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir_valor(arvore)
        elif opcao == "2":
            buscar_valor(arvore)
        elif opcao == "3":
            remover_valor(arvore)
        elif opcao == "4":
            exibir_em_ordem(arvore)
        elif opcao == "5":
            exibir_pre_ordem(arvore)
        elif opcao == "6":
            exibir_pos_ordem(arvore)
        elif opcao == "7":
            mostrar_min_max(arvore)
        elif opcao == "8":
            mostrar_resumo(arvore)
        elif opcao == "9":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()