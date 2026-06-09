from lista_encadeada.No import No

aluna1 = No("Ana")

aluna2 = No("Maria")

aluna1.proximo = aluna2

#print(aluna1.dado)

while aluna1 is not None:

    print(aluna1.dado)

    aluna1 = aluna1.proximo