# ### Exercício 1 — Implementando a pilha

# Implemente uma classe `Pilha` usando nós.

# A classe deve ter:

# - `push(elem)`
# - `pop()`
# - `__len__()`
# - `__repr__()`

# ### Regras

# - use a ideia de cabeça da lista;
# - o topo da pilha deve estar no início da estrutura.

from Pilha import Pilha


if __name__ == "__main__":
    pilha = Pilha()
    pilha.push(10)
    pilha.push(20)
    pilha.push(30)

    print(pilha)

    print(len(pilha))

    pilha.pop() == 30
    pilha.pop() == 20
    pilha.pop() == 10

    print("Pilha funcionando!")
    print(pilha)