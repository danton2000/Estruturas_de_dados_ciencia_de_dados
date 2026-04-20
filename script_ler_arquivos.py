import os

# diretorio_atual = os.getcwd()

# print(diretorio_atual)

def pegar_arquivos_pasta(pasta):
    lista_arquivos = os.listdir(pasta)

    for nome_arquivo in lista_arquivos:

        if ".txt" in nome_arquivo:
            print(nome_arquivo)
        else:
            print(f"Acessando a pasta: {nome_arquivo}")
            pegar_arquivos_pasta(f"{pasta}/{nome_arquivo}")

    print(lista_arquivos)

pegar_arquivos_pasta("Arquivos")

