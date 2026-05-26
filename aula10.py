pilha = []

pilha.append(10)

pilha.append(20)

pilha.append(30)

print(pilha)

print(pilha[-1])

elemento = pilha.pop()

print(elemento)

print(pilha)

##
palavra = "Cebola"

contrario = []

for letra in palavra:
    # o método append() é usado para adicionar um elemento ao final da lista
    contrario.append(palavra[-1])
    # a cada iteração, a variável palavra é atualizada para conter a string sem o último caractere
    # slices
    palavra = palavra[0:-1]
    #print(palavra)

# print(palavra)

# print(contrario)

###
palavra = list("Cebola")

contrario = []

while len(palavra) > 0:
    contrario.append(palavra.pop())
print(contrario)

# Função com pilha
def push(pilha, valor):
    pilha.append(valor)

def pop(pilha):
    if len(pilha) > 0:

        elemnto = pilha.pop()

        return elemnto
    else:
        return None
    
def peek(pilha):
    if len(pilha) > 0:
        return pilha[-1]
    else:
        return None
    
def is_empty(pilha):
    return len(pilha) == 0

def size(pilha):
    return len(pilha)

estrutura = []

push(estrutura, "A")

push(estrutura, "B")

push(estrutura, "C")

print(estrutura)

pop(estrutura)

print(estrutura)

print(peek(estrutura))

pop(estrutura)

pop(estrutura)

pop(estrutura)

print(is_empty(estrutura))

##
# Descobrir se um ( foi fechado por um ) ou não

def verifica_parenteses(expressao):
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

print(verifica_parenteses(")()"))

###
# A Notação Polonesa Reversa, ou RPN, é uma forma de escrever expressões matemáticas em que os operadores aparecem depois dos operandos.

# Exemplo:
# 3 4 +
 
# Significa:
# 3 + 4

# Com pilha(forma simples e basica):

# 1. Lê `3`: empilha.
# 2. Lê `4`: empilha.
# 3. Lê `+`: remove `4`, remove `3`, soma e empilha o resultado.

def rpn(expressao):
    # lista para simular a pilha
    pilha = []
    # iterar sobre cada token na expressão
    for token in expressao.split():
        # se o token for um número, converte para inteiro e empilha
        if token.isdigit():
            # o método append() é usado para adicionar um elemento ao final da lista
            pilha.append(int(token))
        # se o token for um operador, desempilha os dois últimos números, realiza a operação e empilha o resultado
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

print(rpn("3 4 +"))  # Output: 7
