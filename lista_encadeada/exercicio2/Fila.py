from No import No


class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self._size = 0

    def enqueue(self, elem):
        novo_no = No(elem)

        if self.fim is None:
            self.inicio = novo_no
            self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no

        self._size += 1

    def dequeue(self):
        if self.inicio is None:
            raise IndexError("Fila vazia")

        elemento = self.inicio.dado
        self.inicio = self.inicio.proximo

        if self.inicio is None:
            self.fim = None

        self._size -= 1
        return elemento

    def __len__(self):
        return self._size

    def __repr__(self):
        elementos = []
        atual = self.inicio

        while atual is not None:
            elementos.append(atual.dado)
            atual = atual.proximo

        return f"Fila({elementos})"
