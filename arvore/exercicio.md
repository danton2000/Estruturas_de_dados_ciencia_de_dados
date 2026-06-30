# Exercicio

## Dados os elementos, inseridos na ordem abaixo:

50, 30, 70, 20, 40, 60, 80, 35, 45, 65

Monte a arvore resultante e responda:

                 50
                /  \
              30    70
              / \   / \
            20  40 60  80
                /\   \
               35 45  65

menor fica a esquerda
maior a direita

a) Quem é a raiz da arvore ? 50

b) Quem são os nós folha? 20, 35, 45, 65, 80(os aque não tem filho)

c) Quem é o pai do nó 40? 30

d) Quem são os irmãos do nó 60 ? 80

e) Quais os ancestrais do nó 45? 40, 30, 50

f) Quais os descendentes do nó 70 ? 60, 65, 80

g) Qual a saida do percurso em ordem, pós-ordem e pré=ordem
ordem: [20, 30, 35, 40, 45, 50, 60, 65, 70, 80]

pós-ordem: [20, 35, 45, 40, 30, 65, 60, 80, 70, 50]
(pega o elemento mais a esquerda possivel)

pré=ordem: [50, 30, 20, 40, 35, 45, 70, 60, 65, 80]