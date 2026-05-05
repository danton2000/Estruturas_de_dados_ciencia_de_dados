class TabelaHash:

    def __init__(self, tamanho):

        self.tamanho = tamanho

        self.tabela = []

        for i in range(self.tamanho):

            self.tabela.append([])

    def indice(self, chave):

        print(len(chave) % self.tamanho) 
    
    def inserir(self, chave, valor):

        ind = self.indice(chave, len(self.tabela))

        print(ind)

    def buscar(self, chave):

        ind = self.indice(chave, len(self.tabela))

        for item in self.tabela[ind]:

            if item[0] == chave:

                return item[1]
        
        return None
    
    def listar(self):

        print(self.tabela)
    
aluno = TabelaHash(5)

aluno.inserir("Danton", "C")

aluno.inserir("Gabriela", "A")

aluno.inserir("Donizete", "A")

aluno.inserir("Enzo", "B")

aluno.inserir("Larissa", "B")

aluno.listar()