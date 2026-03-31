import numpy as np

estudantes = [
    ("E01", "Ana"),
    ("E02", "Bruno"),
    ("E03", "Carla"),
    ("E04", "Diego"),
    ("E05", "Eduarda"),
    ("E06", "Felipe"),
    ("E07", "Giovana"),
    ("E08", "Henrique")
]

oficinas = {
    "O101": {"nome": "Python para Dados", "sala": "Lab 1", "turno": 0},
    "O102": {"nome": "Design com IA", "sala": "Lab 2", "turno": 0},
    "O103": {"nome": "Robótica Criativa", "sala": "Maker", "turno": 1},
    "O104": {"nome": "Visualização de Dados", "sala": "Lab 1", "turno": 1}
}

inscricoes = {
    "E01": ("O101", "O104"),
    "E02": ("O101", "O103"),
    "E03": ("O102",),
    "E04": ("O101", "O102", "O103"),
    "E05": ("O104",),
    "E06": ("O103", "O104"),
    "E07": ("O102", "O103"),
    "E08": ("O101",)
}

presencas = {
    "O101": {"E01", "E02", "E04", "E08"},
    "O102": {"E03", "E04"},
    "O103": {"E02", "E04", "E06", "E07"},
    "O104": {"E01", "E05"}
}

salas = ("Lab 1", "Lab 2", "Maker")

capacidade = np.array([
    [30, 25],
    [20, 20],
    [15, 18]
])

# Etapa 1: Organização inicial dos dados
# Nesta primeira parte, o objetivo é transformar e organizar os dados de forma que o restante da análise fique mais fácil.
# O programa deverá:
# Criar uma estrutura que associe o código do estudante ao nome.
list_estudante = []

#percorrendo a lista de tuplas
for item in estudantes: 
    #print(item)

    # criando dicionario para cada aluno
    dict_estudante = {
        "codigo": item[0],
        "nome": item[1]
    }

    # guardando o aluno em uma lista
    list_estudante.append(dict_estudante)

#print(list_estudante)

# criando uma lista com as inscricoes
lista_inscricoes = []
for key, value in inscricoes.items():

    inscricao = {
        "codigo": key,
        "codigo_oficina": value
    }

    lista_inscricoes.append(inscricao)

# Criando um novo atributo no dicionario de cada aluno
for item in list_estudante:
    item["inscricoes"] = []

# Percorrendo a lista de estudante
for item in list_estudante:

    #print(item["codigo"])

    # Percorrendo a lista de inscricoes
    for inscricao in lista_inscricoes:

        # Se os codigos baterem
        if item["codigo"] in inscricao["codigo"]:
            
            # Vincular o codigo das incricoes no dicionario dos estudantes
            item["inscricoes"] = inscricao["codigo_oficina"]

# criando uma lista com as oficinas
lista_oficinas = []
for key, value in oficinas.items():

    oficina = {
        "codigo": key,
        "nome": value["nome"]
    }

    lista_oficinas.append(oficina)

# jutando as informações de estudanes, inscricoes e oficinas
lista_nome_oficina = []
for item in list_estudante:

    # Percorrer a inscrição
    for inscricao in item["inscricoes"]:

        # Percorrendo a oficina
        for oficina in lista_oficinas:

            # verificando se a insicricao tem na oficica pelo codigo
            if inscricao in oficina["codigo"]:

                # guarda os nomes dessas oficinas
                lista_nome_oficina.append(oficina["nome"])

            # atualiza o atributo inscricoes de tupla de codigos para uma lista com o nome das oficinas
            item["inscricoes"] = lista_nome_oficina

    # limpa essa lista para a reutilização
    lista_nome_oficina = []

# Exibir de forma organizada em quais oficinas cada estudante está inscrito.
for index, aluno in enumerate(list_estudante):

    print()
    print(f"Estudande {aluno["nome"]} está inscrito nas oficias:")
    for inscricao in aluno["inscricoes"]:
        print(inscricao)
        

# Calcular quantos estudantes estão inscritos em cada oficina.
for index, aluno in enumerate(list_estudante):
    print()
    print(f"Estudande {aluno["nome"]} está inscrito em:")
    print(len(aluno["inscricoes"]), "diciplinas")

# Nesta etapa, pensem com cuidado sobre como percorrer listas de tuplas e como montar novos dicionários a partir das informações já existentes.

# Etapa 2: Análise utilizando conjuntos
# Agora, vocês deverão utilizar operações com conjuntos para extrair novas informações.
# O programa deverá identificar:

# Quais estudantes participaram de mais de uma oficina.
# criando uma lista com as inscricoes

for key, value in inscricoes.items():

   if len(value) > 1:
       print(f"Estudande {key} paricipou de mais de uma oficina")


# Quais estudantes se inscreveram em oficinas, mas não aparecem em nenhuma lista de presença.
set_inscricoes = set(inscricoes)

# Formatando os dados para criar o conjunto dos alunos(set)
list_estudante = []
for key, value in presencas.items():

    for codigo in value:

        list_estudante.append(codigo)

set_list_estudante = set(list_estudante)

print(set_inscricoes - set_list_estudante)

print("Todos compareceram")

# Quais estudantes participaram de oficinas dos dois turnos.

# Aqui não consegui pensar em uma resolução utilizando conjuntos...

# Quais oficinas possuem pelo menos um estudante em comum.