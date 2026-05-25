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