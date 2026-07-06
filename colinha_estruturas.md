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

### Exemplo em Python
```python
pilha = []
pilha.append(10)
pilha.append(20)
pilha.append(30)

print(pilha.pop())  # 30
print(pilha.pop())  # 20
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

### Exemplo em Python
```python
fila = []
fila.append("Ana")
fila.append("Bruno")
fila.append("Carlos")

print(fila.pop(0))  # Ana
print(fila.pop(0))  # Bruno
```

### Vantagem
- Mantém a ordem de chegada
- Muito usada em sistemas e algoritmos

---

## 4. Árvore Binária de Busca (BST)

### Conceito
Uma árvore é uma estrutura hierárquica formada por nós.

Uma árvore binária de busca tem as seguintes regras:
- Cada nó pode ter no máximo dois filhos
- Filho da esquerda tem valor menor que o pai
- Filho da direita tem valor maior que o pai

### Exemplo
```text
    50
   /  \
  30   70
 / \   / \
20 40 60 80
```

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

## 5. Diferença prática entre as estruturas

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

## 6. Comparação rápida

| Estrutura | Ordem | Exemplo de uso |
|---|---|---|
| Pilha | LIFO | histórico, desfazer |
| Fila | FIFO | atendimento, filas |
| Árvore | Hierárquica | busca e organização de dados |

---

## 7. Dicas para prova

- Lembre-se do nome das regras:
  - Pilha = LIFO
  - Fila = FIFO

- Lembre-se de exemplos cotidianos
- Entenda a diferença entre inserir e remover em cada estrutura
- Para árvore, lembre-se da regra do filho esquerdo e direito
- Para árvore binária de busca, saiba que a busca é mais eficiente que em listas lineares em muitos casos

---

## 8. Resumo final em 1 minuto

- Pilha: entra e sai pelo topo
- Fila: entra pelo fim e sai pela frente
- Árvore: organiza dados em nós e ramos

Se você quiser, eu também posso transformar isso em uma versão ainda mais curta, tipo “colinha de prova” com linguagem bem resumida e direta.
