# Atividade Prática

# Estruturas de Dados em Python: Tuplas, Dicionários e Conjuntos

# Introdução:
# Nesta atividade, você irá aplicar os conceitos estudados sobre tuplas, dicionários e conjuntos em situações que envolvem organização, consulta, validação e análise de dados. Além do uso dessas estruturas, será necessário mobilizar conhecimentos anteriores de lógica de programação, como entrada e saída de dados, estruturas condicionais, laços de repetição e manipulação de variáveis. 

# Leia cada situação com atenção e procure pensar não apenas em como fazer o programa funcionar, mas também em por que determinada estrutura é mais adequada para cada caso.

# 1. Cadastro fixo de filme com desempacotamento
# Uma plataforma de streaming deseja registrar informações básicas de um filme de forma que esses dados não possam ser alterados ao longo da execução do programa. 

# Para isso, desenvolva um programa que crie uma tupla contendo as seguintes informações sobre um filme: título, ano de lançamento, duração em minutos e gênero.
filme = (
    {
        "Titulo": "Super Mario",
        "Ano Lancamento": 2022,
        "Duracao": 80,
        "Genero": "Aventura"
    }
)

print(filme)

# Depois de criar a tupla, faça o desempacotamento desses valores de duas formas diferentes:

# a) Primeiro, realize um desempacotamento tradicional, armazenando cada valor em uma variável própria.
titulo = filme["Titulo"]
ano_lancamento = filme["Ano Lancamento"]
duracao = filme["Duracao"]
genero = filme["Genero"]

# b) Depois, realize um novo desempacotamento em que o título fique em uma variável separada e todas as demais informações sejam agrupadas em outra variável utilizando o operador *.
v_titulo, *lista_infomacoes = filme

# Na sequência, exiba os dados do filme em frases organizadas, de modo que fique claro o que cada informação representa.
print(f"Filme do {titulo} do genero {genero}, foi lançado no ano de {ano_lancamento} e dura {duracao} minutos")

# Ao final, escreva um comentário no código explicando por que o uso de uma tupla faz sentido nessa situação, considerando as características dessa estrutura e a natureza fixa dessas informações em um cadastro.
print("A Estrutura Tupla garante uma consistencia e integridade no armazenamento das informações.")

# 2. Análise de registro de usuário ignorando parte dos dados
# Considere que um sistema armazenou os dados de um usuário na seguinte tupla:
usuario = ("Ana", 25, "Brasil", "Premium")

# Crie um programa que faça o desempacotamento dessa tupla, mas ignorando uma das informações com o uso de _. Nesse caso, desconsidere o país e armazene apenas o nome, a idade e o tipo de conta nas variáveis que julgar mais adequadas.
nome, idade, _, tipo_conta = usuario

# Depois disso, exiba uma mensagem apresentando o usuário, mostrando pelo menos seu nome e o tipo de conta.
print(f"Usuaria {nome}, tem {idade} anos e tem uma conta {tipo_conta}")

# Na sequência, percorra a tupla com um laço de repetição e mostre todos os seus valores individualmente na tela.
for dado in usuario:
    print(dado)

# Por fim, explique com um comentário ou com uma mensagem no próprio programa qual é a diferença entre acessar elementos por índice e utilizar desempacotamento, e em que tipo de situação cada estratégia pode ser mais útil.
print("È viavel utilizar o desempacotamento em um tupla, caso for necessario a atualização de alguem dado nessa tupla. " \
"Acessando só a tupla não é permitido alterar seus dados")

# 3. Perfil de lead
# Uma empresa da área de marketing digital deseja armazenar informações sobre um possível cliente interessado em seus serviços. Para isso, crie um programa que monte um dicionário com pelo menos os seguintes dados de um lead: nome, idade e origem do contato.  

lead = {
    "Nome": "Danton",
    "Idade": 25,
    "Origem": "Instagram"
}

# Depois de criar esse dicionário, o programa deve:
# a) Exibir o dicionário completo.
print(lead)
# b) Alterar a origem do lead para um novo valor definido por você.
lead["Origem"] = "Facebook"

# c) Adicionar um novo campo chamado interesse, indicando qual produto, curso ou serviço chamou a atenção desse lead.
lead["Interesse"] = "Curso de Python"

# d) Percorrer o dicionário utilizando .items(), exibindo cada chave e seu respectivo valor.
for chave, valor in lead.items():
    print(f"{chave}: {valor}")
# Ao final, apresente uma frase-resumo com base nas informações armazenadas, como se o sistema estivesse gerando uma pequena síntese do perfil do lead.
print(f"O lead {lead['Nome']} tem {lead['Idade']} anos, entrou em contato através do {lead['Origem']} e tem interesse em {lead['Interesse']}.")

# 5. Controle de presença sem repetição

# Durante uma oficina, a lista de presença foi preenchida várias vezes pelos participantes, o que gerou nomes repetidos. A lista registrada foi a seguinte:
presencas = ["Ana", "Bruno", "Carlos", "Ana", "Daniel", "Bruno", "Ana"]
# Desenvolva um programa que transforme essa lista em um set, eliminando automaticamente os nomes duplicados.

# Depois disso, o programa deve:
# a) Mostrar quantas pessoas realmente participaram da oficina.
participantes_unicos = set(presencas)
print(f"Participaram da oficina {len(participantes_unicos)} pessoas.")
# b) Percorrer o conjunto e exibir os nomes dos participantes.
for participante in participantes_unicos:
    print(participante)
# c) Escrever uma breve explicação, em forma de comentário no código ou mensagem final, sobre por que o uso de sets foi adequado para esse problema.
print("O uso de sets é adequado para esse problema porque eles não permitem elementos duplicados, garantindo que cada nome seja registrado apenas uma vez, o que é ideal para controlar a presença sem repetição.")

# 6. Monitoramento de acessos por período do dia
# Uma plataforma educacional deseja analisar quais usuários acessaram o sistema ao longo de um determinado dia. Para isso, a equipe de tecnologia decidiu separar os acessos em dois períodos: manhã e tarde. No entanto, como uma mesma pessoa pode acessar o sistema várias vezes no mesmo turno, é necessário tratar duplicidades antes de fazer a análise.

# Crie um programa que monte duas listas com nomes de usuários: uma para os acessos da manhã e outra para os acessos da tarde. Essas listas devem ser construídas com dados informados pelo usuário. Para isso, utilize laços de repetição e permita que a pessoa digite vários nomes para cada período. Você pode definir uma palavra de parada, como "fim", para encerrar o cadastro de cada turno.

# Função para coletar nomes de usuários
def coletar_nomes(periodo):
    nomes = []
    print(f"Digite os nomes dos usuários que acessaram no período da {periodo}.")
    print("Digite 'fim' para encerrar o cadastro.")
    while True:
        nome = input(f"Nome ({periodo}): ").strip()
        if nome.lower() == "fim":
            break
        if nome:  # Evitar entradas vazias
            nomes.append(nome)
    return nomes

# Coletar nomes para os dois períodos
manha = coletar_nomes("manhã")
tarde = coletar_nomes("tarde")

# Depois de preencher as duas listas, o programa deve convertê-las em sets para remover nomes repetidos dentro de cada período.

manha_set = set(manha)
tarde_set = set(tarde)

# Na sequência, faça uma análise dos dados e mostre:
# a) Quais usuários acessaram o sistema nos dois períodos do dia.
acessos_comuns = manha_set & tarde_set
print("Usuários que acessaram nos dois períodos:")
for usuario in acessos_comuns:
    print(usuario)

# b) Quais usuários acessaram apenas pela manhã.
acessos_manha = manha_set - tarde_set
print("Usuários que acessaram apenas pela manhã:")
for usuario in acessos_manha:
    print(usuario)

# c) Quais usuários acessaram apenas pela tarde.
acessos_tarde = tarde_set - manha_set
print("Usuários que acessaram apenas pela tarde:")
for usuario in acessos_tarde:
    print(usuario)

# d) Quantos usuários únicos acessaram a plataforma ao longo do dia inteiro.
acessos_unicos = manha_set | tarde_set
print(f"Quantidade de usuários únicos que acessaram a plataforma ao longo do dia: {len(acessos_unicos)}")


# Ao final, apresente uma pequena conclusão no próprio programa ou em comentário no código, explicando por que o uso de conjuntos foi mais adequado do que o uso de listas para esse tipo de análise.
print("O uso de conjuntos foi mais adequado para esse tipo de análise porque eles permitem realizar operações de união, interseção e diferença de forma eficiente, facilitando a identificação de usuários que acessaram em diferentes períodos e garantindo a exclusão de duplicatas, o que é essencial para uma análise precisa dos acessos.")

# Neste exercício, procure organizar bem o fluxo de entrada e saída, de modo que o programa seja fácil de testar e compreender.

# 7. Sistema de votação com menu

# Desenvolva um programa para registrar votos em uma enquete sobre qual tema os alunos gostariam de estudar na próxima aula. As opções disponíveis são: Python, IA, Banco de Dados e Web.

# O programa deve utilizar um laço de repetição com while para permitir vários votos sucessivos. A cada voto válido, um dicionário deve ser atualizado com a quantidade de votos de cada tema.

# O sistema só deve encerrar quando o usuário digitar "fim". Caso o usuário informe uma opção que não existe, o programa deve exibir uma mensagem de erro e não contabilizar esse voto.

# Ao final da votação, percorra o dicionário e mostre quantos votos cada tema recebeu. Depois, informe qual foi o tema mais votado pela turma.

# Procure construir uma interação clara, organizada e fácil de usar, como se esse sistema pudesse ser utilizado de fato em sala de aula.

# Sistema de votação para escolha de tema da próxima aula

# Opções disponíveis para votação
opcoes = ["Python", "IA", "Banco de Dados", "Web"]

# Dicionário para armazenar os votos
votos = {opcao: 0 for opcao in opcoes}

print("Bem-vindo ao sistema de votação!")
print("Escolha um dos temas abaixo para votar:")
for opcao in opcoes:
    print(f"- {opcao}")
print("Digite 'fim' para encerrar a votação.")

# Laço de repetição para registrar os votos
while True:
    voto = input("Digite o tema escolhido: ").strip()
    if voto.lower() == "fim":
        break
    elif voto in votos:
        votos[voto] += 1
        print(f"Voto registrado para {voto}!")
    else:
        print("Opção inválida! Escolha uma das opções disponíveis.")

# Exibir o resultado da votação
print("\nResultado da votação:")
for tema, quantidade in votos.items():
    print(f"{tema}: {quantidade} votos")

# Determinar o tema mais votado
tema_mais_votado = max(votos, key=votos.get)
print(f"\nO tema mais votado foi: {tema_mais_votado} com {votos[tema_mais_votado]} votos!")

# 8. Organização de inscrições em minicursos
# Uma instituição está oferecendo três minicursos durante uma semana acadêmica: Python, Inteligência Artificial e Visualização de Dados. Os dados das inscrições vieram com alguns problemas: há estudantes repetidos, estudantes inscritos em mais de um curso e nomes que precisam ser analisados de forma mais organizada. Para isso, utilize as seguintes listas:

python = ["Ana", "Bruno", "Carlos", "Ana", "Daniel", "Eduarda"]
ia = ["Bruno", "Fernanda", "Carlos", "Gabriel", "Bruno", "Helena"]
visualizacao = ["Ana", "Carlos", "Igor", "Julia", "Helena", "Igor"]

# Crie um programa que transforme cada uma dessas listas em sets, removendo duplicatas. Em seguida, o programa deve identificar:

set_python = set(python)
set_ia = set(ia)
set_visualizacao = set(visualizacao)

# a) Quais estudantes estão inscritos em todos os três minicursos.
estudantes_todos_cursos = set_python & set_ia & set_visualizacao


# b) Quais estudantes estão inscritos em pelo menos dois minicursos.
estudantes_dois_cursos = (set_python & set_ia) | (set_python & set_visualizacao) | (set_ia & set_visualizacao)

# c) Quais estudantes estão inscritos em apenas um minicurso.
estudantes_um_curso = (set_python | set_ia | set_visualizacao) - (set_python & set_ia) - (set_python & set_visualizacao) - (set_ia & set_visualizacao)

# d) A lista completa de todos os estudantes inscritos em pelo menos um dos cursos.
estudantes_todos = set_python | set_ia | set_visualizacao

# Depois disso, crie um dicionário chamado relatorio, em que cada chave seja o nome de um estudante e cada valor seja uma tupla contendo duas informações: a quantidade de minicursos em que esse estudante está inscrito e uma classificação textual correspondente.

# Utilize as seguintes regras para a classificação:
# 3 cursos: "inscrição máxima"
# 2 cursos: "inscrição múltipla"
# 1 curso: "inscrição única"

relatorio = {}

for estudante in estudantes_todos:
    quantidade_cursos = sum([estudante in set_python, estudante in set_ia, estudante in set_visualizacao])
    if quantidade_cursos == 3:
        classificacao = "inscrição máxima"
    elif quantidade_cursos == 2:
        classificacao = "inscrição múltipla"
    elif quantidade_cursos == 1:
        classificacao = "inscrição única"
    else:
        classificacao = "sem inscrição"
    relatorio[estudante] = (quantidade_cursos, classificacao)

# Na sequência, percorra o dicionário e exiba um relatório organizado na tela, com frases como:

for estudante, (quantidade, classificacao) in relatorio.items():
    print(f"{estudante} está inscrito em {quantidade} minicurso(s) e seu status é {classificacao}.")

# Ana está inscrita em 2 minicursos e seu status é inscrição múltipla.

# Por fim, o programa deve entrar em um laço com while, perguntando ao usuário o nome de um estudante para consulta. Se o nome existir no dicionário, o sistema deve mostrar suas informações. Caso não exista, deve informar que o estudante não foi encontrado. O programa só deve encerrar quando o usuário digitar "sair".

while True:
    consulta = input("Digite o nome do estudante para consulta (ou 'sair' para encerrar): ").strip()
    if consulta.lower() == "sair":
        print("Encerrando o programa. Até mais!")
        break
    elif consulta in relatorio:
        quantidade, classificacao = relatorio[consulta]
        print(f"{consulta} está inscrito em {quantidade} minicurso(s) e seu status é {classificacao}.")
    else:
        print(f"Estudante '{consulta}' não encontrado no relatório.")