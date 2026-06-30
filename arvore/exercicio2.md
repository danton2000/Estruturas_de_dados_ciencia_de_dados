# Exercicio

## Dados os elementos, inseridos na ordem abaixo:

21, 26, 30, 33, 47, 52, 29, 55, 37, 19, 31

Monte a arvore resultante e responda:

                 21
                /  \
              19    26
                      \
                       30
                        /\
                       29 33
                           /\
                         31  47
                             /\
                           37  52
                                \
                                 55

pré ordem: [21, 19, 26, 30, 29, 33, 31, 47, 37, 52, 55]
(raiz, depois sempre a esquerda, se não tiver mais, vai a direita)

pos ordem: [19, 29, 31, 37, 55, 52, 47, 33, 30, 23, 21]
(pegando a esquerda, todas as esquerdas, depois a direita, até a raiz)