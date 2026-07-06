# Colinha de Estruturas de Dados

## 1. O que são estruturas de dados?

Estruturas de dados são formas de organizar e armazenar dados para facilitar o acesso, a busca, a inserção e a remoção.

Elas ajudam a resolver problemas de forma mais eficiente.

Exemplo simples:
- guardar nomes em uma lista
- organizar tarefas em fila
- controlar etapas em uma pilha

---

## 2. Pilha (Stack)

### Conceito
Uma pilha é uma estrutura do tipo LIFO:
- Last In, First Out
- O último elemento que entra é o primeiro a sair

### Exemplo do cotidiano
- Pilha de pratos
- Histórico de páginas do navegador
- Desfazer ações em um editor

### Operações principais
- push: adicionar um elemento no topo
- pop: remover o elemento do topo
- peek: ver o elemento do topo sem remover
- is_empty: verificar se está vazia

### Exemplo simples
```text
Empilha 10
Empilha 20
Empilha 30

Remove -> 30
Remove -> 20
```

### Exemplo com nós
```python
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

# ideia de pilha: o último que entra é o primeiro a sair
n1 = No(10)
n2 = No(20)
n3 = No(30)

n1.proximo = n2
n2.proximo = n3

# topo da pilha = 30
```

### Vantagem
- Simples de usar
- Ótima para controle de fluxo e reversão

---

## 3. Fila (Queue)

### Conceito
Uma fila é uma estrutura do tipo FIFO:
- First In, First Out
- O primeiro elemento que entra é o primeiro a sair

### Exemplo do cotidiano
- Fila de banco
- Fila de atendimento
- Processamento de tarefas em ordem

### Operações principais
- enqueue: adicionar no fim
- dequeue: remover do início
- front: ver o primeiro sem remover
- is_empty: verificar se está vazia

### Exemplo simples
```text
Entra Ana
Entra Bruno
Entra Carlos

Sai Ana
Sai Bruno
Sai Carlos
```

### Exemplo com nós
```python
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

# ideia de fila: quem entra primeiro sai primeiro
n1 = No("Ana")
n2 = No("Bruno")
n3 = No("Carlos")

n1.proximo = n2
n2.proximo = n3
```

### Vantagem
- Mantém a ordem de chegada
- Muito usada em sistemas e algoritmos

---

## 4. Lista Encadeada

### Conceito
Uma lista encadeada é uma estrutura em que cada elemento é um nó, e cada nó aponta para o próximo.

Diferente de uma lista comum, não é necessário que os elementos fiquem em posições consecutivas na memória.

### Estrutura de um nó
Cada nó normalmente possui:
- um valor
- uma referência para o próximo nó

### Exemplo visual
```text
[10] -> [20] -> [30] -> None
```

### Vantagens
- Fácil de inserir e remover no início
- Não precisa redimensionar como uma lista tradicional

### Desvantagens
- Acesso direto é mais lento
- Para encontrar um elemento, muitas vezes é preciso percorrer a lista

### Exemplo simples em Python
```python
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

n1 = No(10)
n2 = No(20)
n3 = No(30)

n1.proximo = n2
n2.proximo = n3
```

Isso significa:
```text
10 -> 20 -> 30
```

### Ideia prática
- cada nó guarda um valor
- cada nó aponta para o próximo
- assim a lista fica encadeada

### Quando usar
- Quando você precisa de muitas inserções e remoções
- Quando não sabe quantos elementos terá no início

---

## 5. O que é um nó?

Um nó é um bloco básico de uma estrutura encadeada ou de uma árvore.

Ele guarda:
- um dado
- uma ou mais referências para outros nós

### Exemplo
Em uma lista encadeada:
- o nó guarda o valor
- aponta para o próximo nó

Em uma árvore:
- o nó guarda o valor
- aponta para os filhos da esquerda e da direita

### Ideia principal
O nó é a “peça” que conecta os elementos da estrutura.

---

## 6. Árvore Binária de Busca (BST)

### Conceito
Uma árvore é uma estrutura hierárquica formada por nós.

Uma árvore binária de busca tem as seguintes regras:
- Cada nó pode ter no máximo dois filhos
- Filho da esquerda tem valor menor que o pai
- Filho da direita tem valor maior que o pai

### Exemplo simples
```text
    50
   /  \
  30   70
```

Cada nó pode ter dois filhos:
- 30 é filho da esquerda de 50
- 70 é filho da direita de 50

### Exemplo com nós
```python
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

raiz = No(50)
raiz.esquerda = No(30)
raiz.direita = No(70)
```

### Ideia prática
- a árvore cresce em forma de ramos
- cada nó pode apontar para dois filhos

### Conceitos que costumam cair na prova
- Inserção: o valor vai para a esquerda se for menor e para a direita se for maior
- Busca: compara o valor com o nó atual e segue para a subárvore certa
- Remoção: remove o nó e reorganiza a árvore
- Mínimo e máximo: o menor fica sempre à esquerda mais profunda; o maior, à direita mais profunda
- Folhas: nós sem filhos
- Altura: quantidade de níveis da árvore
- Balanceamento: a diferença entre a altura das subárvores não pode ser grande

### Vantagens
- Busca mais rápida que listas em muitos casos
- Organização hierárquica dos dados

### Operações principais
- inserir
- buscar
- remover
- percorrer a árvore

### Percursos principais
- Pré-ordem: raiz → esquerda → direita
- Em ordem: esquerda → raiz → direita
- Pós-ordem: esquerda → direita → raiz

### Exemplo de percurso em ordem
Para a árvore acima, o resultado seria:
```text
20, 30, 40, 50, 60, 70, 80
```

---

## 7. Diferença prática entre as estruturas

### Pilha
- Útil quando a ordem de saída importa ao contrário
- Ex.: desfazer ação

### Fila
- Útil quando a ordem de chegada importa
- Ex.: atendimento

### Árvore
- Útil para organizar dados de forma hierárquica
- Ex.: buscas rápidas, cadastros, menus e estruturas de decisão

---

## 8. Comparação rápida

| Estrutura | Ordem | Exemplo de uso |
|---|---|---|
| Pilha | LIFO | histórico, desfazer |
| Fila | FIFO | atendimento, filas |
| Árvore | Hierárquica | busca e organização de dados |

---

## 9. Dicas para prova

- Lembre-se do nome das regras:
  - Pilha = LIFO
  - Fila = FIFO

- Lembre-se de exemplos cotidianos
- Entenda a diferença entre inserir e remover em cada estrutura
- Para árvore, lembre-se da regra do filho esquerdo e direito
- Para árvore binária de busca, saiba que a busca é mais eficiente que em listas lineares em muitos casos

---

## 10. Resumo final em 1 minuto

- Pilha: entra e sai pelo topo
- Fila: entra pelo fim e sai pela frente
- Árvore: organiza dados em nós e ramos

Se você quiser, eu também posso transformar isso em uma versão ainda mais curta, tipo “colinha de prova” com linguagem bem resumida e direta.
