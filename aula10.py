"""aula10.py
Exemplos e utilitários de pilha para aulas.

Este arquivo contém vários exemplos demonstrativos organizados em funções:
- exemplo 1: uso básico de lista como pilha
- exemplo 2: inverter string com slicing
- exemplo 3: inverter string usando lista + pop
- exemplo 4: API simples de pilha (`push`, `pop`, `peek`, `is_empty`, `size`)
- exemplo 5: verificação de parênteses balanceados
- exemplo 6: avaliador RPN (Notação Polonesa Reversa)

Execute o arquivo diretamente para ver as saídas de cada exemplo.
"""

def example_basic_stack():
    """Exemplo 1: operações básicas com lista usada como pilha."""
    pilha = []
    pilha.append(10)
    pilha.append(20)
    pilha.append(30)
    print("Basic stack:", pilha)
    print("Top element:", pilha[-1])
    elemento = pilha.pop()
    print("Popped element:", elemento)
    print("After pop:", pilha)


def example_reverse_string_slicing():
    """Exemplo 2: inverter uma string usando slicing e acumulação."""
    palavra = "Cebola"
    contrario = []
    # em cada iteração pegamos o último caractere da string e encurtamos
    for _ in palavra:
        contrario.append(palavra[-1])
        palavra = palavra[0:-1]
    print("Reversed (slicing):", "".join(contrario))


def example_reverse_using_stack():
    """Exemplo 3: inverter uma string convertendo-a em lista e usando pop."""
    palavra = list("Cebola")
    contrario = []
    while len(palavra) > 0:
        contrario.append(palavra.pop())
    print("Reversed (stack):", "".join(contrario))


# Funções que implementam uma API simples de pilha
def push(pilha, valor):
    """Empilha `valor` no fim da lista `pilha`."""
    pilha.append(valor)


def pop(pilha):
    """Desempilha e retorna o último elemento de `pilha`, ou `None` se vazia."""
    if len(pilha) > 0:
        elemento = pilha.pop()
        return elemento
    else:
        return None


def peek(pilha):
    """Retorna o topo da pilha sem remover, ou `None` se vazia."""
    if len(pilha) > 0:
        return pilha[-1]
    else:
        return None


def is_empty(pilha):
    """Retorna True se a pilha estiver vazia."""
    return len(pilha) == 0


def size(pilha):
    """Retorna o tamanho da pilha."""
    return len(pilha)


def example_stack_api_demo():
    """Exemplo 4: demonstração da API de pilha definida acima."""
    estrutura = []
    push(estrutura, "A")
    push(estrutura, "B")
    push(estrutura, "C")
    print("Stack API - after pushes:", estrutura)
    pop(estrutura)
    print("After one pop:", estrutura)
    print("Peek:", peek(estrutura))
    pop(estrutura)
    pop(estrutura)
    pop(estrutura)  # tentar pop em pilha vazia (retorna None)
    print("Is empty:", is_empty(estrutura))


def verifica_parenteses(expressao):
    """Verifica se os parênteses em `expressao` estão balanceados.

    Retorna True se toda abertura '(' tiver um fechamento ')', caso contrário False.
    """
    pilha = []
    for char in expressao:
        if char == '(':
            pilha.append(char)
        elif char == ')':
            if len(pilha) > 0:
                pilha.pop()
            else:
                return False
    return len(pilha) == 0


def example_parentheses_check():
    """Exemplo 5: teste rápido da verificação de parênteses."""
    print("Parentheses ' )() ' balanced?:", verifica_parenteses(")()"))


def rpn(expressao):
    """Avalia uma expressão em Notação Polonesa Reversa (RPN).

    Suporta operadores: +, -, *, /
    Tokens devem ser separados por espaço, por exemplo: '3 4 +'
    """
    pilha = []
    for token in expressao.split():
        if token.isdigit():
            pilha.append(int(token))
        else:
            b = pilha.pop()
            a = pilha.pop()
            if token == '+':
                pilha.append(a + b)
            elif token == '-':
                pilha.append(a - b)
            elif token == '*':
                pilha.append(a * b)
            elif token == '/':
                pilha.append(a / b)
    return pilha[0]


def example_rpn():
    """Exemplo 6: avaliação RPN simples."""
    print("RPN '3 4 +':", rpn("3 4 +"))


if __name__ == "__main__":
    example_basic_stack()
    print("---")
    example_reverse_string_slicing()
    print("---")
    example_reverse_using_stack()
    print("---")
    example_stack_api_demo()
    print("---")
    example_parentheses_check()
    print("---")
    example_rpn()
