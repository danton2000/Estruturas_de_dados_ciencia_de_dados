class TabelaHash:

    def __init__(self, tamanho):

        self.tamanho = tamanho

        self.tabela = []

        for i in range(self.tamanho):

            self.tabela.append([])

    def indice(self, chave):

        print(len(chave) % self.tamanho) 
    
    def inserir(self, chave, valor):

        pass

    def buscar(self, chave):

        ind = self.indice(chave, len(self.tabela))

        for item in self.tabela[ind]:

            if item[0] == chave:

                return item[1]
        
        return None
    
    def listar(self):

        print(self.tabela)
    
aluno = TabelaHash(7)

aluno.inserir("ana", 1)

aluno.inserir("bia", 2)

aluno.inserir("carlos", 3)

aluno.inserir("daniel", 4)

aluno.listar()