conjunto = []

for i in range(5): # Aqui nem precisa do i, ele ta so para darmos um nome para cada numero que vai passar 
   # Aqui ele vai de 0 a 4 
   numero = int(input("Digite um número: "))
   conjunto.append(numero)

print(conjunto)

conjunto.sort()
print(conjunto)

conjunto.sort(reverse=True)
print(conjunto)

maior = max(conjunto)
print(maior)

menor = min(conjunto)
print(menor)

soma = sum(conjunto)
media = soma / len(conjunto)
print(media)
