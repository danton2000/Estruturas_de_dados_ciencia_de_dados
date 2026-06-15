# ### Exercício 2 — Implementando a fila

# Implemente uma classe `Fila` usando nós.

# A classe deve ter:

# - `enqueue(elem)`
# - `dequeue()`
# - `__len__()`
# - `__repr__()`

# ### Regras

# - a remoção deve acontecer no início;
# - a inserção deve acontecer no final.

from Fila import Fila

if __name__ == "__main__":
    fila = Fila()
    fila.enqueue(10)
    fila.enqueue(20)
    fila.enqueue(30)

    print(fila)

    print(len(fila))
    fila.dequeue() == 10
    fila.dequeue() == 20
    fila.dequeue() == 30

    print("Fila funcionando!")
    print(fila)