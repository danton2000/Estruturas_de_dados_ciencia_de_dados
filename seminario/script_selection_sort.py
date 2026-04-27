"""
Exemplo com Selection Sort em lista encadeada simples.

Explicação leiga:
- Selection Sort procura o menor elemento a cada iteração e coloca ele
  na posição correta (começando da esquerda). Repetindo esse processo, a
  lista fica ordenada.
"""
class Node:
    def __init__(self, numero):
        self.valor = numero
        self.proximo = None

class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def add_valor(self, valor):
        """Adiciona um nó ao final."""
        novo_no = Node(valor)

        if self.inicio is None:
            self.inicio = novo_no
            self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no


    def imprime_lista(self):
        """Imprime todos os valores da lista do início ao fim."""
        if self.inicio is None:
            print("A lista está vazia.")
        else:
            no_atual = self.inicio
            while no_atual is not None:
                print(f"Valor: {no_atual.valor}")
                no_atual = no_atual.proximo

    def selection_sort(self):
        """
        Ordena a lista encadeada em ordem crescente usando Selection Sort.

        Estratégia (versão simples que troca valores dentro dos nós):
        - Para cada posição da lista (nó `i`), encontra o nó com o menor
          valor entre `i` e o final.
        - Troca o valor do nó `i` com o valor do nó que contém o mínimo.

        Observações:
        - Mantemos a simplicidade trocando apenas os valores dos nós em vez
          de reencadear ponteiros.
        - Complexidade: O(n^2) no pior caso e no caso médio.
        """
        if self.inicio is None:
            return

        i = self.inicio
        # 'i' representa a posição atual que vamos preencher com o menor valor
        while i:
            # Encontrar o nó com o menor valor a partir de i
            menor = i
            j = i.proximo
            while j:
                if j.valor < menor.valor:
                    menor = j
                j = j.proximo

            # Se menor for diferente de i, troca os valores
            if menor is not i:
                i.valor, menor.valor = menor.valor, i.valor

            # Avança para a próxima posição
            i = i.proximo


if __name__ == "__main__":
    lista_desordenada = [5, 3, 8, 1, 2]
    lista = Lista()
    for numero in lista_desordenada:
        lista.add_valor(numero)

    print("Lista Desordenada.")
    lista.imprime_lista()

    lista.selection_sort()
    print("Lista Ordenada.")
    lista.imprime_lista()