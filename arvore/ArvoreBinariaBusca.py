from No import No

class ArvoreBinariaBusca:
    # Arvore otimizada para encontrar valores
    def __init__(self):
        self.raiz = None

    def is_empty(self):
        return self.raiz == None
    
    def insert(self, valor):
        if self.is_empty():
            self.raiz = No(valor)

            return True

        atual = self.raiz

        while True:

            # Se o valor for menor, vai para a esquerda
            if valor < atual.dado:
                if atual.esquerda == None:
                    atual.esquerda = No(valor)

                    return True
                else:
                    atual = atual.esquerda
            # Se o valor for maior, vai para a direita        
            elif valor > atual.dado:
                if atual.direita == None:
                    atual.direita = No(valor)

                    return True
                else:
                    atual = atual.direita
            else:
                # Valor já existe na árvore, não insere duplicatas
                return False
    
    def search(self, valor):
        atual = self.raiz

        while atual is not None:
            
            if valor == atual.dado:
                return atual
            
            if valor < atual.dado:
                atual = atual.esquerda

            else:
                atual = atual.direita

        return None
    
    def pre_order(self):

        valores = []

        self._pre_order(self.raiz, valores)

        return valores

    def _pre_order(self, no, valores):

        if no is None:
            # Caso base: nó vazio, retorna
            return
        
        # Processa o nó atual (adiciona seu valor à lista de valores)
        valores.append(no.dado)  # Processa o nó atual

        # Continua a travessia pré-ordem: primeiro a subárvore esquerda, depois a direita
        self._pre_order(no.esquerda, valores)

        # Continua a travessia pré-ordem: primeiro a subárvore esquerda, depois a direita
        self._pre_order(no.direita, valores)