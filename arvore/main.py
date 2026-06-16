from ArvoreBinariaBusca import ArvoreBinariaBusca

if __name__ == "__main__":
    arvore = ArvoreBinariaBusca()

    arvore.insert(10)
    arvore.insert(5)
    arvore.insert(15)
    arvore.insert(3)
    arvore.insert(7)
    arvore.insert(12)
    arvore.insert(18)

    print(arvore.search(7).dado)  # Deve imprimir 7
    print(arvore.search(4))          # Deve imprimir None (não encontrado)

    print(arvore.pre_order())        # Deve imprimir [10, 5, 3, 7, 15, 12, 18]