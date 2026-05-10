lista_vendas = [
    {"id": 100, "cliente": "Ana"},
    {"id": 101, "cliente": "Bruna"},
    {"id": 102, "cliente": "Raquel"},
    {"id": 103, "cliente": "Borges"},
    {"id": 104, "cliente": "Franco"},
    {"id": 105, "cliente": "Pedro"},
    {"id": 106, "cliente": "Gardel"},
    {"id": 107, "cliente": "Fleck"},
    {"id": 108, "cliente": "Daniel"},
]

def busca_venda_por_id(lista_vendas, id):
    
    for venda in lista_vendas:
        # print(venda)
        if venda["id"] == id:
            print(f"Venda {venda["id"]} do cliente {venda["cliente"]} localizada.")

            break
        else:
            print("Venda não localizada.")

busca_venda_por_id(lista_vendas, 103)

## tabela hash
def criar_tabela(tamanho):

    tabela = []

    for i in range(tamanho):

        tabela.append([])

    return tabela

def indice(chave, tamanho):

    return len(chave) % tamanho

print(indice("humberto", 5))

def inserir(tabela, chave, valor):

    ind = indice(chave, len(tabela))

    tabela[ind].append((chave,valor))

def buscar(tabela, chave):

    ind = indice(chave, len(tabela))

    for item in tabela[ind]:

        if item[0] == chave:

            return item[1]
        
    return None

aluno = criar_tabela(7)

inserir(aluno, "Danton", "C")

inserir(aluno, "Gabriela", "A")

inserir(aluno, "Donizete", "A")

inserir(aluno, "Enzo", "B")

inserir(aluno, "Larissa", "B")

print(aluno)

print(buscar(aluno, "Danton"))