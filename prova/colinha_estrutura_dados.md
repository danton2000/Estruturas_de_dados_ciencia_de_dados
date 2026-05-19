# 📚 COLINHA — Estrutura de Dados e Algoritmos

---

# 🧠 Big O (Complexidade)

Resumo do conteúdo:

Big O: mede como o tempo ou espaço do algoritmo cresce com o tamanho da entrada. Ignora constantes e termos de menor ordem.

O(1): constante
O(n): linear
O(log n): logarítmica
O(n²): quadrática
Pilha (stack): LIFO, último a entrar é o primeiro a sair. Em Python, append() para push e pop() para pop.

Recursividade: função chama ela mesma. Precisa de caso base e passo recursivo.

Busca linear: percorre cada elemento até encontrar. Complexidade O(n). Bom para listas pequenas ou não ordenadas.

Busca binária: divide a lista ordenada ao meio e descarta metade a cada passo. Complexidade O(log n). Exige lista ordenada.

Tabela hash (dicionário): associa chave a valor por meio de hash, permite acesso rápido. Colisões ocorrem quando duas chaves geram mesmo índice; podem ser tratadas com encadeamento (lista no mesmo índice).

Ordenação:

Bubble Sort: compara e troca vizinhos. O(n²).
Selection Sort: escolhe menor e troca. O(n²).
Insertion Sort: insere elementos na posição correta. O(n²).
Merge Sort: divide e junta ordenado. O(n log n).
Quick Sort: escolhe pivô e particiona menores/maiores. Média O(n log n), pior O(n²).
Boas práticas para analisar complexidade:

foque em repetições
verifique complexidade de funções/métodos usados
considere o termo de maior ordem
Exemplos de análise:

t(n) = 4 + 3n => O(n)
t(n) = 2 => O(1)
algoritmo com laço até encontrar elemento: melhor caso O(1), pior caso O(n)
laços aninhados: O(n²)
soma de O(n) + O(n log n) => O(n log n)

📌 Mostra quantos passos um algoritmo executa conforme os dados aumentam.

👉 Ignoramos constantes:
```python
2n + 5 → O(n)
```

## Principais complexidades

| Big O | Nome | Ideia |
|---|---|---|
| O(1) | Constante | sempre igual |
| O(n) | Linear | percorre lista |
| O(log n) | Logarítmica | divide no meio |
| O(n²) | Quadrática | dois loops |

---

## Exemplos

### O(1)
```python
lista[0]
```

### O(n)
```python
for i in lista:
    print(i)
```

### O(n²)
```python
for i in lista:
    for j in lista:
        print(i, j)
```

---

# 📚 Pilha (Stack)

📌 Último que entra = primeiro que sai

#️⃣ LIFO  
(Last In, First Out)

## Exemplos reais
- Pilha de pratos
- Ctrl + Z
- Histórico navegador

## Operações
```python
pilha = []

pilha.append(10) # push
pilha.pop()      # pop
```

---

# 🔁 Recursividade

📌 Função chama ela mesma.

## Precisa:
- Caso base → para execução
- Passo recursivo → continua

## Exemplo
```python
def contar(n):
    if n == 0:
        return

    print(n)
    contar(n - 1)
```

---

# 🔎 Busca Linear

📌 Percorre elemento por elemento.

## Exemplo
```python
lista = [3,7,2,9]

for i in lista:
    if i == 2:
        print("Encontrou")
```

📌 Complexidade:
#️⃣ O(n)

✅ Boa para:
- listas pequenas
- listas desordenadas

---

# 🔍 Busca Binária

📌 Divide a lista no meio.

⚠️ Precisa lista ordenada.

## Exemplo
Lista:
```python
[1,2,3,4,5,6,7]
```

Busca o 5:
- meio = 4
- 5 é maior
- busca direita

📌 Complexidade:
#️⃣ O(log n)

✅ Muito rápida.

---

# 🗂️ Tabela Hash

📌 Estrutura que:
- recebe chave
- calcula índice
- guarda valor

👉 Acesso rápido.

## Exemplo
```python
dados = {
    "nome": "Lucas"
}

print(dados["nome"])
```

---

# 📌 Função Hash

Transforma chave em índice.

```python
hash("nome")
```

---

# 📌 Colisão

Duas chaves → mesmo índice.

Exemplo:
```python
101 e 108 → índice 3
```

---

# 📌 Encadeamento

Mesmo índice guarda lista.

```python
indice 3:
[101, 108]
```

---

# 🔃 Métodos de Ordenação

---

# 📌 Bubble Sort

## O que faz?
Compara vizinhos e troca.

## Exemplo
```python
[5,3]
→ [3,5]
```

## Como funciona?
- compara lado a lado
- maior vai “subindo”

📌 Complexidade:
#️⃣ O(n²)

---

# 📌 Selection Sort

## O que faz?
Procura menor elemento e troca.

## Exemplo
```python
[5,3,1]
→ [1,3,5]
```

## Como funciona?
- encontra menor valor
- coloca na posição correta

📌 Complexidade:
#️⃣ O(n²)

---

# 📌 Insertion Sort

## O que faz?
Insere elemento na posição correta.

## Exemplo
```python
[5,3]
→ [3,5]
```

## Como funciona?
- pega elemento
- move para posição correta

📌 Complexidade:
#️⃣ O(n²)

---

# 📌 Merge Sort

## O que faz?
Divide lista e junta ordenado.

## Exemplo
```python
[5,2,8,1]

→ [5,2] [8,1]

→ [2,5] [1,8]

→ [1,2,5,8]
```

📌 Complexidade:
#️⃣ O(n log n)

✅ Muito eficiente.

---

# 📌 Quick Sort

## O que faz?
Escolhe pivô.

Separa:
- menores
- maiores

## Exemplo
```python
[5,2,8,1]

pivô = 5

menores:
[2,1]

maiores:
[8]
```

📌 Complexidade média:
#️⃣ O(n log n)

📌 Pior caso:
#️⃣ O(n²)

---

# 🚨 RESUMÃO PRA PROVA

| Conteúdo | Ideia |
|---|---|
| Big O | custo algoritmo |
| Pilha | LIFO |
| Recursão | função chama ela mesma |
| Linear | percorre tudo |
| Binária | divide no meio |
| Hash | acesso rápido |
| Bubble | troca vizinhos |
| Selection | procura menor |
| Insertion | insere ordenado |
| Merge | divide e junta |
| Quick | usa pivô |

class TabelaHash:

    def __init__(self, tamanho):

        self.tamanho = tamanho

        self.tabela = []

        for i in range(self.tamanho):

            self.tabela.append([])

    def indice(self, chave):

        print(len(chave) % self.tamanho) 
    
    def inserir(self, chave, valor):

        ind = self.indice(chave, len(self.tabela))

        print(ind)

    def buscar(self, chave):

        ind = self.indice(chave, len(self.tabela))

        for item in self.tabela[ind]:

            if item[0] == chave:

                return item[1]
        
        return None
    
    def listar(self):

        print(self.tabela)
    
aluno = TabelaHash(5)

aluno.inserir("Danton", "C")

aluno.inserir("Gabriela", "A")

aluno.inserir("Donizete", "A")

aluno.inserir("Enzo", "B")

aluno.inserir("Larissa", "B")

aluno.listar()