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

## Exercício 2 — Soma dos valores

# Implemente o método `sum_values()`, que devolve a soma de todos os valores armazenados na árvore.

# Exemplo:

# ```
#        10
#       /  \
#      5    15

# sum_values() -> 30

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
# ```

## Exercício 4 — Remover o menor valor

# Implemente `remove_min()`, que remove o menor valor da árvore e retorna esse valor. Caso a árvore esteja vazia, retorne `None`.

# Dica: o menor valor é o nó mais à esquerda; depois de encontrá-lo, reaproveite a ideia dos casos de remoção.

## Exercício 5 — Verificar se a árvore está balanceada

# Crie o método `is_balanced()`.

# Para este exercício, considere uma árvore balanceada quando, em todos os nós, a diferença entre a contagem dos nos da subárvore esquerda e os nos da subárvore direita for no máximo `1`.

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