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

    def em_order(self):

        valores = []

        self._em_order(self.raiz, valores)

        return valores
    
    # Recursividade, impilha e desempilha, para percorrer a árvore em ordem (esquerda, raiz, direita)
    
    def _em_order(self, no, valores):

        if no is None:
            # Caso base: nó vazio, retorna
            return
        
        # Continua a travessia em-ordem: primeiro a subárvore esquerda
        self._em_order(no.esquerda, valores)

        # Processa o nó atual (adiciona seu valor à lista de valores)
        valores.append(no.dado)  # Processa o nó atual

        # Continua a travessia em-ordem: depois a subárvore direita
        self._em_order(no.direita, valores)

    def pos_order(self):

        valores = []

        self._pos_order(self.raiz, valores)

        return valores
    
    def _pos_order(self, no, valores):
        if no is None:
            # Caso base: nó vazio, retorna
            return
        
        # Continua a travessia pós-ordem: primeiro a subárvore esquerda, depois a direita
        self._pos_order(no.esquerda, valores)

        # Continua a travessia pós-ordem: primeiro a subárvore esquerda, depois a direita
        self._pos_order(no.direita, valores)

        # Processa o nó atual (adiciona seu valor à lista de valores)
        valores.append(no.dado)  # Processa o nó atual

    def minimo(self):

        if self.is_empty():
            return None
        
        atual = self.raiz

        while atual.esquerda is not None:

            atual = atual.esquerda

        return atual.dado
    
    def maximo(self):

        if self.is_empty():
            return None
        
        atual = self.raiz

        while atual.direita is not None:

            atual = atual.direita

        return atual.dado
    
    def contar_nos(self):

        return self._contar_nos(self.raiz)
    
    def _contar_nos(self, no):

        if no is None:

            return 0

        return(
            1 + self._contar_nos(no.esquerda) + self._contar_nos(no.direita)
        )
    
    def contar_folhas(self):

        return self._contar_folhas(self.raiz)
    
    def _contar_folhas(self, no):

        if no is None:
            return 0
        
        if no.esquerda is None and no.direita is None:

            return 1
        
        return (
            self._contar_folhas(no.esquerda) + self._contar_folhas(no.direita)
        )

    def remove(self, valor):

        self.raiz, removido = self._remove(self.raiz, valor)

    def _remove(self, no, valor):
        
        if no is None:

            return None, False
        
        if valor < no.dado:

            no.esquerda, removido = self._remove(no.esquerda, valor)

            return no, removido
        
        if valor > no.dado:

            no.direita, removido = self._remove(no.direita, valor)

            return no, removido
        
        if no.esquerda is None and no.direita is None:

            return None, True
        
        if no.esquerda is None:
            
            return no.direita, True

        if no.direita is None:
            
            return no.esquerda, True
        
        sucessor = self._minimo_no(no.direita)
        
        no.dado = sucessor.dado

        no.direita, _ = self._remove(no.direita, sucessor.valor)

    def _minimo_no(self, no):

        atual = no

        while atual.esquerda is not None:

            atual = atual.esquerda

        return atual

    def contains(self, valor):
        atual = self.raiz

        while atual is not None:
            if valor == atual.dado:
                return True

            if valor < atual.dado:
                atual = atual.esquerda
            else:
                atual = atual.direita

        return False
    
    def sum_values(self):
        return self._sum_values(self.raiz)

    def _sum_values(self, no):
        if no is None:
            return 0

        return no.dado + self._sum_values(no.esquerda) + self._sum_values(no.direita)
    
    def sum_even_values(self):
        return self._sum_even_values(self.raiz)

    def _sum_even_values(self, no):
        if no is None:
            return 0

        total = self._sum_even_values(no.esquerda) + self._sum_even_values(no.direita)

        if no.dado % 2 == 0:
            total += no.dado

        return total
    
    def remove_min(self):
        if self.is_empty():
            return None

        valor, self.raiz = self._remove_min(self.raiz)
        return valor

    def _remove_min(self, no):
        if no is None:
            return None, None

        if no.esquerda is None:
            return no.dado, no.direita

        valor, no.esquerda = self._remove_min(no.esquerda)
        return valor, no
    
    def is_balanced(self):
        return self._is_balanced(self.raiz)

    def _is_balanced(self, no):
        if no is None:
            return True

        esquerda = self._altura(no.esquerda)
        direita = self._altura(no.direita)

        if abs(esquerda - direita) > 1:
            return False

        return self._is_balanced(no.esquerda) and self._is_balanced(no.direita)

    def _altura(self, no):
        if no is None:
            return 0

        return 1 + max(self._altura(no.esquerda), self._altura(no.direita))
    
    def altura(self):
        return self._altura(self.raiz)