def bubble_sort(lista):

    trocou = True

    while trocou:

        trocou = False

        for j in range(len(lista) - 1):
            
            if lista[j] > lista[j + 1]:
                
                print(f"Lista sendo ordenada: {lista}")

                lista[j], lista[j + 1] = lista[j + 1], lista[j]

                trocou = True
    
    return lista

lista = [4,2,7,1,3]

print(f"Lista original: {lista}")
print(f"Lista ordenada: {bubble_sort(lista)}")

# Lista original: [4, 2, 7, 1, 3]
# Lista sendo ordenada: [4, 2, 7, 1, 3]
# Lista sendo ordenada: [2, 4, 1, 3, 7]
# Lista sendo ordenada: [2, 1, 3, 4, 7]
# Lista sendo ordenada: [1, 2, 3, 4, 7]
# Lista ordenada: [1, 2, 3, 4, 7]