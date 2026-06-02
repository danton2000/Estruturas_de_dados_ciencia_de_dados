# Exercicio 1
# Adicionar na fila
# Remover da fila
# Verificar o primeiro elemento da fila
# Mostrar o tamanho da fila

lista_fila = []

# Adicionando elementos na fila, sempre no final.
def enqueue(fila, valor):
    """Enfileira `valor` no fim da lista `fila`."""
    fila.append(valor)

# Removendo elementos da fila, sempre do inicio.
def dequeue(fila):
    """Desenfileira o primeiro elemento da lista `fila`."""
    if len(fila) > 0:
        return fila.pop(0)

# Mostrando o primeiro elemento da fila, sem remover.
def front(fila):
    """Retorna o primeiro elemento da lista `fila`."""
    if len(fila) > 0:
        return fila[0]

# Mostrando o tamanho da fila.
def size(fila):
    """Retorna o tamanho da lista `fila`."""
    return len(fila)

enqueue(lista_fila, "10")

enqueue(lista_fila, "20")

enqueue(lista_fila, "30")

print(lista_fila)

print(size(lista_fila))

print(dequeue(lista_fila))

print(front(lista_fila))

print(lista_fila)

# Exercicio 2
from collections import deque

fila = deque()

fila.append("A")

fila.append("B")

fila.append("C")

print(fila)

print(fila[0])

primeiro = fila.popleft()

print(primeiro)

print(fila)

if (len(fila) > 0):
    fila.popleft()

print(fila)

# Exercicio 3
# Adicionar na fila
# Remover da fila
# Verificar o primeiro elemento da fila
# Mostrar o tamanho da fila
# Usando deque

print("Exercicio 3 - Usando deque")

fila = deque()

fila.append("A")
fila.append("B")
fila.append("C")

print(fila)

def enqueue(fila, valor):
    """Adicionando valor na final, sempre no inicio"""
    fila.append(valor)

def dequeue(fila):
    """Removendo valor do inicio da fila"""
    if len(fila) > 0:
        return fila.popleft()
    
def front(fila):
    """Mostrando o primeiro elemento da fila, sem remover."""
    if len(fila) > 0:
        return fila[0]

def size(fila):
    """Mostrando o tamanho da fila."""
    return len(fila)

enqueue(fila, "D")

print(fila)

print(front(fila))

dequeue(fila)

print(fila)

print(size(fila))