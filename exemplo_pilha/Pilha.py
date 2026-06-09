class Pilha:
    """
    Implementação de uma pilha (stack) em Python.
    A pilha é uma estrutura de dados do tipo LIFO (Last In, First Out),onde o último elemento inserido é o primeiro a ser removido.
    A classe Pilha possui os seguintes métodos:
    - push(item): Adiciona um item ao topo da pilha.
    - pop(): Remove e retorna o item do topo da pilha. Se a pilha estiver vazia, lança uma exceção IndexError.
    - peek(): Retorna o item do topo da pilha sem removê-lo. Se a pilha estiver vazia, lança uma exceção IndexError.
    - is_empty(): Retorna True se a pilha estiver vazia, caso contrário, retorna False.
    - size(): Retorna o número de itens na pilha.
    - __repr__(): Retorna uma representação em string da pilha.
    """

    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pilha vazia")
            #return None
        else:
            elemento = self._items.pop()
            return elemento    

    def peek(self):
        if self.is_empty():
            raise IndexError("Pilha vazia")
            #return None
        else:
            return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0
    
    def size(self):
        return len(self._items)
    
    def __repr__(self):
        
        return f"Stack({self._items})"