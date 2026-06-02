from Queue import *

fila = Queue()

fila.enqueue("Gabriela")

fila.enqueue("João")

fila.enqueue("Maria")

fila.enqueue("Pedro")

print(fila)

print("Primeiro elemento da fila:", fila.front())

print("Removendo o primeiro elemento da fila:", fila.dequeue())

print(fila)

print("Removendo o primeiro elemento da fila:", fila.dequeue())

print("Removendo o primeiro elemento da fila:", fila.dequeue())

print("Removendo o primeiro elemento da fila:", fila.dequeue())

print(fila)
