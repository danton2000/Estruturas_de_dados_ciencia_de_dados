# A classe No representa um nó em uma lista encadeada,
from No import No

# A classe ListaEncadeada representa uma lista encadeada, 
# que é uma estrutura de dados composta por nós (No) que estão ligados entre si. 
# Cada nó contém um dado e uma referência para o próximo nó na lista.
class ListaEncadeada:
    
    def __init__(self):
        # O head é o primeiro nó da lista, inicialmente é None porque a lista está vazia
        self.head = None

        # O size é o número de elementos na lista, inicialmente é 0 porque a lista está vazia
        self._size = 0

    # Função para adicionar um elemento no final da lista
    def append(self, elemento):
        novo_no = No(elemento)

        # Se a lista já tiver elementos, percorre até o final e adiciona o novo nó
        if self.head:
            atual = self.head

            # Percorre a lista até o último nó
            while atual.proximo is not None:
                atual = atual.proximo

            # Adiciona o novo nó no final da lista
            atual.proximo = novo_no
        
        else:
            # Se a lista estiver vazia, o novo nó se torna o head da lista
            self.head = novo_no
        
        # Incrementa o tamanho da lista
        self._size += 1
    
    # O método __repr__ é usado para representar a lista encadeada como uma string,
    # mostrando os elementos da lista em ordem, separados por " -> ".
    def __repr__(self):
        
        texto = ""

        atual = self.head

        while atual:

            texto += f"{atual.dado} -> "

            atual = atual.proximo

        return texto
    
    # O método __len__ é usado para retornar o número de elementos na lista encadeada,
    # permitindo que a função len() seja usada para obter o tamanho da lista.
    def __len__(self):
        return self._size
    
    # O método __getitem__ é usado para acessar um elemento da lista encadeada pelo seu índice,
    # permitindo que a sintaxe de indexação (lista[index]) seja usada para obter o elemento correspondente 
    # ao índice fornecido.

    def __getitem__(self, index):
        
        atual = self.head

        for i in range(index):
            if atual:
                atual = atual.proximo
            else:
                raise IndexError("Índice fora do alcance da lista encadeada.")
        
        return atual.dado
    
    # O método __setitem__ é usado para modificar um elemento da lista encadeada pelo seu índice,
    # permitindo que a sintaxe de indexação (lista[index] = valor) seja usada 
    # para atribuir um novo valor ao elemento correspondente ao índice fornecido.
    def __setitem__(self, index, valor ):

        atual = self.head

        for i in range(index):
            if atual:
                atual = atual.proximo
            else:
                raise IndexError("Índice fora do alcance da lista encadeada.")
        
        atual.dado = valor
    
    def remove(self, elemento):

        if self.head is None:
            raise ValueError("A lista encadeada está vazia.")
        
        if self.head.dado == elemento:
            
            self.head = self.head.proximo
            
            self._size -= 1
            
        else:
            anterior = self.head

            atual = anterior.proximo

            while atual:

                if atual.dado == elemento:
                    anterior.proximo = atual.proximo

                    atual.proximo = None

                    self._size -= 1
                
                anterior = atual

                atual = atual.proximo