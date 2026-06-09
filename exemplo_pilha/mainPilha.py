from exemplo_pilha.Pilha import Pilha

print(Pilha.__doc__)

p1 = Pilha()

p1.push("Cebola")

p1.push("Limão")

p1.push("Abobora")

print(p1)

print(p1.peek())

print(p1.pop())

print(p1)