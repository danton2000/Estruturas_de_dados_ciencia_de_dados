def potencia(base, expoente):
    
    valor = base * expoente

    print(valor)

    if expoente <= 1:
        return valor

    return base * potencia(base, expoente-1)

print(potencia(base = 5, expoente = 2))

# print(5 ** 2)
# 25

