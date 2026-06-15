from No import No

class Pilha:
    def __init__(self):
        self.topo = None
        self._size = 0

    def push(self, elem):
        novo_no = No(elem)
        novo_no.proximo = self.topo
        self.topo = novo_no
        self._size += 1

    def pop(self):
        if self.topo is None:
            raise IndexError("Pilha vazia")

        elemento = self.topo.dado
        self.topo = self.topo.proximo
        self._size -= 1
        return elemento

    def __len__(self):
        return self._size

    def __repr__(self):
        elementos = []
        atual = self.topo

        while atual is not None:
            elementos.append(atual.dado)
            atual = atual.proximo

        return f"Pilha({elementos})"