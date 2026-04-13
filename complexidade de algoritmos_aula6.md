### **O que é Complexidade de Algoritmos?**
A **complexidade** mede **quantos passos** um algoritmo precisa para resolver um problema, dependendo do tamanho da entrada. Isso nos ajuda a saber se o algoritmo é eficiente.

Existem dois tipos principais:
1. **Complexidade de Tempo**: Quantos passos o algoritmo executa.
2. **Complexidade de Espaço**: Quanta memória o algoritmo usa.

---

### **Tipos de Complexidade de Tempo**
Aqui estão os tipos mais comuns, do mais rápido ao mais lento:

1. **O(1) - Constante**
   - O algoritmo executa **sempre o mesmo número de passos**, não importa o tamanho da entrada.
   - Exemplo:
     ```python
     def constante(lista):
         return lista[0]  # Sempre pega o primeiro elemento
     ```
   - **Exemplo real**: Acessar um elemento específico de uma lista.

2. **O(n) - Linear**
   - O número de passos cresce **proporcionalmente ao tamanho da entrada**.
   - Exemplo:
     ```python
     def linear(lista):
         for item in lista:
             print(item)  # Percorre todos os elementos
     ```
   - **Exemplo real**: Percorrer uma lista inteira.

3. **O(n²) - Quadrática**
   - O número de passos cresce **com o quadrado do tamanho da entrada**.
   - Exemplo:
     ```python
     def quadratica(lista):
         for i in lista:
             for j in lista:
                 print(i, j)  # Compara todos com todos
     ```
   - **Exemplo real**: Comparar todos os pares de elementos.

4. **O(log n) - Logarítmica**
   - O número de passos cresce **muito devagar** conforme a entrada aumenta.
   - Exemplo:
     ```python
     def logaritmica(lista, alvo):
         inicio, fim = 0, len(lista) - 1
         while inicio <= fim:
             meio = (inicio + fim) // 2
             if lista[meio] == alvo:
                 return meio
             elif lista[meio] < alvo:
                 inicio = meio + 1
             else:
                 fim = meio - 1
     ```
   - **Exemplo real**: Busca binária (dividir a lista ao meio a cada passo).

5. **O(2ⁿ) - Exponencial**
   - O número de passos **dobra** a cada aumento na entrada.
   - Exemplo:
     ```python
     def exponencial(n):
         if n == 0:
             return 1
         return exponencial(n - 1) + exponencial(n - 1)
     ```
   - **Exemplo real**: Resolver problemas de combinação ou permutação.

---

### **Como Identificar a Complexidade?**
1. **Olhe para os laços (loops):**
   - Um laço simples que percorre todos os elementos → **O(n)**.
   - Um laço dentro de outro (aninhado) → **O(n²)**.

2. **Considere operações específicas:**
   - Acessar um elemento de uma lista → **O(1)**.
   - Remover um elemento de uma lista → **O(n)** (porque desloca os elementos).

3. **Divisão e conquista:**
   - Se o algoritmo divide o problema em partes menores (como busca binária) → **O(log n)**.

4. **Soma de complexidades:**
   - Se há várias partes no algoritmo, some as complexidades:
     - Exemplo:
       ```python
       def exemplo(lista):
           for i in lista:  # O(n)
               print(i)
           for j in lista:  # O(n)
               print(j)
       ```
       - Complexidade total: **O(n) + O(n) = O(2n)** → Simplifica para **O(n)**.

---

### **Exemplos do seu código**
1. **`tem_duplicacao`**
   - Dois laços aninhados → **O(n²)**.

2. **`ache_min`**
   - Um laço simples → **O(n)**.

3. **`remover`**
   - Depende do índice:
     - Remover o último → **O(1)**.
     - Remover do início ou meio → **O(n)**.

---

### **Resumo**
- **O(1)**: Operações fixas (ex.: acessar um elemento).
- **O(n)**: Um laço simples (ex.: percorrer uma lista).
- **O(n²)**: Dois laços aninhados (ex.: comparar todos com todos).
- **O(log n)**: Dividir o problema em partes menores (ex.: busca binária).
- **O(2ⁿ)**: Crescimento exponencial (ex.: combinações).

Se precisar de mais exemplos ou explicações, é só pedir!