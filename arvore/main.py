from ArvoreBinariaBusca import ArvoreBinariaBusca

if __name__ == "__main__":
    arvore = ArvoreBinariaBusca()

    arvore.insert(50)
    arvore.insert(30)
    arvore.insert(70)
    arvore.insert(20)
    arvore.insert(40)
    arvore.insert(60)
    arvore.insert(80)
    arvore.insert(35)
    arvore.insert(45)
    arvore.insert(65)

    print(arvore.search(50).dado)  # Deve imprimir 7
    #print(arvore.search(4))          # Deve imprimir None (não encontrado)

    print(arvore.pre_order())        # Deve imprimir [50, 30, 20, 40, 35, 45, 70, 60, 65, 80]

    print(arvore.em_order())         # Deve imprimir [20, 30, 35, 40, 45, 50, 60, 65, 70, 80] ordenada

    print(arvore.pos_order())        # Deve imprimir [20, 35, 45, 40, 30, 65, 80, 70, 60, 50]

    print(arvore.maximo())

    print(arvore.minimo())

    print(arvore.contar_nos)

    print(arvore.contar_folhas)