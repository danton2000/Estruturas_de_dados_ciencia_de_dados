# Crie uma tupla chamada pedidos, com os valores:
# 1023, "Carlos", 89.90

# Faça o desempacotamento dessa tupla em 3 variaves
# id_pedido, cliente_ valor

# Exiba os dados no formato
#     Pedido 1023 feito por Calor no valor de R$ 89.90

pedidos = (1023, "Carlos", 89.90)

id_pedido, cliente, valor = pedidos

print(f"Pedido {id_pedido} feito por {cliente}, no valor de R$ {valor}")

# Crie um dicionario chamado lead, conforme print
lead = {
    "nome": "Juliana",
    "origem": "Instagram",
    "score": 72
}

# Atualize o score para 85
lead["score"] = 85

# Adicione uma nova chave chamada "status"
lead["status"] = None
print(lead)

# Se score >= 80 + "quente" / Caso contrario + "frio"  
lead["status"] = "Quente" if lead["score"] >= 85 else "Frio" 

# Mostre todas as chaves e valores usando .items()
print(lead.items())

# Desafio: Use get() para tentar acessar a chave "telefone", caso não exista, retorne "não informe"
print(lead.get("Telefone", "Não informado"))

# Uma empresa está analisando os dados de usuários cadastrados em sua plataforma.
# Porém, a base possui dados duplicados e inconsistentes.
# Você recebeu duas listas:

cadastros_sistema = ["ana@email.com", "bruno@email.com", "carlos@email.com", "ana@email.com", "dani@email.com"]

emails_validos = {"ana@email.com", "bruno@email.com", "carlos@email.com", "edu@email.com"}

# . Converta cadastros_sistema para um set para remover duplicatas
cadastros_sistema = set(cadastros_sistema)
print(cadastros_sistema)

# · Descubra quais e-mails cadastrados são inválidos
# (ou seja, estão no sistema mas NÃO estão na lista de emails válidos)
#print(cadastros_sistema - emails_validos)

# · Descubra quais e-mails válidos ainda não se cadastraram no sistema
#print(emails_validos - cadastros_sistema)

# · Exiba os resultados com mensagens explicativas, por exemplo:
# · Emails inválidos: { ... }
print(f"Emails inválidos: {cadastros_sistema - emails_validos}")

# · Emails válidos não cadastrados: { ... }
print(f"Emails válidos não cadastrados: {emails_validos - cadastros_sistema}")