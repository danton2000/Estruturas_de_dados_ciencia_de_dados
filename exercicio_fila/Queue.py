from collections import deque

class Queue:

    def __init__(self):
        self._items = deque()
    
    def enqueue(self, item):
        self._items.append(item)

    def is_empty(self):

        if len(self._items) == 0:
            return True
        
        return False

    def dequeue(self):

        if self.is_empty():
            raise IndexError("A fila está vazia.")
        
        return self._items.popleft()
    
    def front(self):

        if self.is_empty():
            raise IndexError("A fila está vazia.")
        
        return self._items[0]
    
    def size(self):
        return len(self._items)
    
    def __str__(self):
        
        return "Fila: " + str(list(self._items)) + " | Tamanho: " + str(self.size()) + " | Vazia: " + str(self.is_empty())
    
