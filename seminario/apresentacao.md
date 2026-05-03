```markdown
# 📊 Selection Sort (Ordenação por Seleção)

## 👥 Integrantes
- Nome 1
- Nome 2
- Nome 3

---

## 🧠 Ideia Geral

O Selection Sort é um algoritmo de ordenação simples.

Ele funciona selecionando o menor elemento da parte não ordenada da lista e colocando ele na posição correta.

### 🔁 Funcionamento:
- Percorre a lista
- Encontra o menor valor
- Troca com a posição atual
- Repete o processo

👉 A cada iteração, um elemento é colocado na posição correta.

---

## 🔍 Passo a Passo

Lista inicial:
```

[5, 3, 8, 1, 2]

```

### 1ª rodada:
- Menor valor: 1
- Troca com 5

```

[1, 3, 8, 5, 2]

```

### 2ª rodada:
- Menor valor: 2
- Troca com 3

```

[1, 2, 8, 5, 3]

```

### 3ª rodada:
- Menor valor: 3
- Troca com 8

```

[1, 2, 3, 5, 8]

```

### Resultado final:
```

[1, 2, 3, 5, 8]

````

---

## 💻 Implementação em Python

```python
def selection_sort(lista):
    # tamanho da lista
    n = len(lista)

    # laço principal
    for i in range(n):
        menor_indice = i
        print(f"Menor indice: {menor_indice}")

        # busca do menor valor
        for j in range(i+1, n):
            print(f"Valor de I: {i}")
            print(f"Valor de J: {j}")

            if lista[j] < lista[menor_indice]:
                print(f"{lista[j]} menor {lista[menor_indice]}")
                menor_indice = j
                print(f"menor_indice: {menor_indice}")

        # troca dos valores
        lista[i], lista[menor_indice] = lista[menor_indice], lista[i]
        print(f"Lista alterada: {lista}")


if __name__ == "__main__":
    lista = [5, 3, 8, 1, 2]

    print("Lista Desordenada.")
    print(lista)

    selection_sort(lista)
````

---

## 🧩 Explicação do Código

* `len(lista)` → obtém o tamanho da lista
* `for i in range(n)` → percorre cada posição
* `menor_indice = i` → assume que o menor é o atual

### 🔎 Loop interno:

* `for j in range(i+1, n)` → percorre o restante da lista
* Compara os valores
* Atualiza o índice do menor elemento

### 🔄 Troca:

```python
lista[i], lista[menor_indice] = lista[menor_indice], lista[i]
```

👉 Coloca o menor valor na posição correta

---

## ⏱️ Complexidade de Tempo

| Caso        | Complexidade |
| ----------- | ------------ |
| Melhor caso | O(n²)        |
| Caso médio  | O(n²)        |
| Pior caso   | O(n²)        |

👉 O algoritmo sempre percorre toda a lista, independente da ordem inicial.

---

## ✅ Vantagens

* Simples de entender
* Fácil de implementar
* Poucas trocas de elementos
* Baixo uso de memória

---

## ❌ Limitações

* Ineficiente para listas grandes
* Complexidade alta (O(n²))
* Não aproveita lista já ordenada

---

## 🎯 Quando usar

* Para aprendizado de algoritmos
* Listas pequenas
* Situações onde o número de trocas precisa ser reduzido

---

## 📌 Conclusão

O Selection Sort é um algoritmo de ordenação simples e didático, ideal para aprendizado.

Apesar de sua facilidade de implementação, ele não é recomendado para grandes volumes de dados devido à sua baixa eficiência.

---

## 📝 Resumo

O Selection Sort é um algoritmo que ordena uma lista selecionando o menor elemento e colocando-o na posição correta a cada iteração. Ele possui complexidade O(n²) em todos os casos, sendo simples, porém ineficiente para grandes conjuntos de dados.

```