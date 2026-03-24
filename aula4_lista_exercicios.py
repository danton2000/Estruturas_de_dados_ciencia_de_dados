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
    
}

# Depois de criar esse dicionário, o programa deve:
# a) Exibir o dicionário completo.
# b) Alterar a origem do lead para um novo valor definido por você.
# c) Adicionar um novo campo chamado interesse, indicando qual produto, curso ou serviço chamou a atenção desse lead.
# d) Percorrer o dicionário utilizando .items(), exibindo cada chave e seu respectivo valor.
# Ao final, apresente uma frase-resumo com base nas informações armazenadas, como se o sistema estivesse gerando uma pequena síntese do perfil do lead.