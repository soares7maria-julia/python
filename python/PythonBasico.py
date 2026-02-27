''' # 1 
print("Hello world")

Usando essas aspas podemos comentar 
varias linhas ao mesmo tempo


# 2 TIPOS DE DADOS
mnemonico = "Maju"
nome = "Anna" # a string deve estar entre " ", ' ' ou até ''' '''( aspas simples triplas
idade = 30         # Inteiro 
altura = 1.67      # Float( numero quebrado)
feminino = True    # Boleano( True ou False)

print("Nao sabia que seria tao facil ~ Ass " + mnemonico)

# isso nao funciona ==> print(nome + " tem " + idade + " anos, sua altura é " + altura + "e é do sexo " + feminino )

# so da para concatenar string com string no print()
# e aqui temos string com inteiro||Float||Boleano

idadestr = '30'
alturastr = '1.67'
femininostr = 'True'

print(nome + " tem " + idadestr + " anos, e sua altura é " + alturastr )

print(nome)
print(feminino)
print(idade)
print(altura)


# 3 FUNÇÕES BASIQUINHAS 

# Aqui para Minusculo e Maiusculo
nome_maior = nome.upper()
nome_menor = nome.lower()

print("É " + nome + " ou " + nome_maior + " ou " + nome_menor)
print(nome.upper())
print(nome.lower())

# O title() deixa a primeira letra de cada palavra em maiuscula
titulo = "Primeira vez no python".title()
print(titulo)

# Devolve True ou False
print(nome_maior.isupper())

# SIM ISSO É POSSIVEL AQUI
print(nome.upper().isupper())
print(nome.lower().isupper())


# 4 SELECINAR UMA CARACTER ESPECIFICO NA STRING

# Para o primeiro
print(nome[0])

# Para selecionar o ultimo 
print(titulo[-1])

# Um conjunto de letras
print(titulo[1:5])
# Ele nao pega o ultimo caracter, entao aqui ele vai devolver os caracteres das posições 1,2,3,4

# Para devolver o caracter de tal posição até o ultimo
print(titulo[12: ])

# MEDIR O TAMANHO DE UMA STRING

print(len(titulo))
# conta tudo, até os espaços

# 5 MUDAR UMA PARTE DA STRING

titulo_segunda = titulo.replace( "Primeira" , "Segunda") 
#deve ser escrita exatamente do jeito que ta na frase

print(titulo_segunda)

# 6 COLOCAR UMA VARIAVEL NO PRINT
nome_Fernanda = "Fernanda"
idade_Fernanda = 26
altura_Fernanda = 1.64


print(f"{nome_Fernanda} tem {idade_Fernanda} e sua altura é de {altura_Fernanda}.")
# Essa é a forma mais util; Colocamos um f no inicio para dizer que tudo que está entre {} é uma variavel.


# 7 COMO LIDAR COM NUMEROS E OPERAÇOES ARITMETICAS

# Pra quando quiser saber o tipo de uma variavel
print(type(idade_Fernanda)) # aqui aparece que idade_Fernanda é da classe dos inteiros("int")
print(type(altura_Fernanda)) #aqui aparece que é um decimal("float")

# Converter variaveis de um tipo para outro
conve_de_texto_para_inteiro = int("40")
conve_de_texto_para_float = float("20.15")

print(type(conve_de_texto_para_inteiro))

print(conve_de_texto_para_float)

# 8 OPERAÇOES ARITMETICAS E FUNÇOES

# ordem das operaçoes
# 1 = o que ta entre ()
# 2 = **(exponenciaçao)
# 3 = * (multiplicaçao), / (divisao), // (divisao sem decimais), % (resto)
# 4 = + (somar), - (subtrair)

soma = 2 + 2
diminuir = 10 - 8
dividir = 10 / 2
multiplicar = 100 * 8
exponenciar =  2 ** 5
dividir_inteiro = 5//2
resto_divisao = 5 % 2

equacao = (10 + 5) * 2 ** 2 - 6 / 3

print(soma)
print(diminuir)
print(dividir)
print(multiplicar)
print(exponenciar)
print(dividir_inteiro)
print(resto_divisao)

print(equacao)

# Funçoes uteis 

numero_maximo = max(3, 12)
numero_minimo = min(4, 10)

rentabilidade_ibovespa = round(0.45634635155, 2)

print(rentabilidade_ibovespa)

# 9 COMO COLETAR DADOS DO USUARIO( simples)

nome_usuario = input("Qual o seu nome? ")

print(f"Ola {nome_usuario}")

idade_usuario = int(input("Qual sua idade? "))
# Deve converter para inteiro(int) se quiser fazer contas

ano_nascimento = 2026 - idade_usuario

print(f"Como você me disse que tem {idade_usuario}, entao seu ano de nascimento deve ser {ano_nascimento}")


# 10 LISTAS E FUNCOES DE LISTAS
lista_de_nomes = ["brenno", "leandro", "lucas"]
#                     0         1         2

lista_de_nomes[0:2]
lista_de_nomes[-1]

bancos = ['Itau', 'Bradesco', 'Banco do Brasil']
preco_acoes = [20, 15, 10]

print(bancos)
print(preco_acoes)

# Adicionar novos dados a listas
bancos.append("Santander")
preco_acoes.append(30)
# (append()) Adiciona um elemento em uma lista  
bancos.append("Nubank")

print(bancos)
print(preco_acoes)


# Iserir um dados em uma posiçao expecifica
bancos.insert(1, "Inter")
print(bancos)

# Remover um item da lista
bancos.remove("Nubank")

#Remove o item de tal posiçao
bancos.remove(bancos[1]) # NAO, isso nao da certo: bancos.remove(1, "Inter")

print(bancos)

# 11 ORDENAR 

# Crescente
# O sort() ordena para ordem crescente
preco_acoes.sort() # Isso NAO funciona:    ordenado = preco_acoes.sort()
print(preco_acoes) #                       print(ordenado)

# Aqui criamos uma nova lista em ondem crescente
crescente = sorted(preco_acoes)
print(f"crescente: {crescente}")

# Decrescente
preco_acoes.sort(reverse=True) # Adicionamos esse reverse=True
print(preco_acoes)

# Aqui criamos uma nova lista em ordem decrescente
decrescente = sorted(preco_acoes, reverse=True)
print(f"decrescente: {decrescente}")

# CONDICIONAIS 

dinheiro = int(input("Quanto voçê tem para investir: "))

if dinheiro >= 1000:
   print("Você deveria investir")

elif dinheiro >= 600 and dinheiro < 1000:      # aqui temos o elif que é a junçao de if e else 
   print("Você pode pensar sobre investir")    # Podemos usar and(e) e o or(ou)

else: 
   print("Talvez seja cedo para investir")
 
# 11 LOOPS 

#  LOOP WHILE 
# O loop nunca para de rodar enquanto a condição nao se satisfaz  
# esse tipo de loop é bem pouco usado
meta = 5
venda = 0

while venda < meta:
   print(f"Total vendas: {venda}. Voce ainda nao alcançou a meta")

   venda = venda + 1  # Se nao tiver essa linha o codigo fica rodando para sempre
                      # Porque sempre será o numero atribuido no inicio (venda = 0)

print("Meta batida, parabens")

# FOR LOOP
bancos2 = ['Itau', 'Bradesco', 'Banco do Brasil']
preco_banco = [20, 15, 10]

for eba in bancos2:    # Esse eba depois do for pode ser chamado de qualquer outra coisa
   print(eba)          # 

for m in range(0, len(bancos2)):     # Aqui o range() faz com que ao invez de aparacer o nome do banco,
   print(m)                          # apareca a posicao dele. len() conta o tamanho do conjunto bancos2
   print(bancos2[m], preco_banco[m]) # aqui aparece o nome e a posicao do banco
   print(f"O banco '{bancos2[m]}' tem um valor de {preco_banco[m]}") 


# Aqui temos o range completo 
# range(inicio, fim, passo)
'''

# Exemplo 1 - Contando de 2 até 9 de 1 em 1
print("Exemplo 1 - Contando de 2 até 9 de 1 em 1")
for i in range(2, 10, 1):
    print(i)

#  Contando de 10 até 1 de 1 em 1 (decrescente)
print("Exemplo 2 - Contando de 10 até 1 de 1 em 1 (decrescente)")
for i in range(10, 0, -1):
    print(i)

# Contando de 10 até 0 de 2 em 2 (decrescente)
print("Exemplo 3 - Contando de 10 até 0 de 2 em 2 (decrescente)")
for i in range(10, -1, -2):
    print(i)

# Contando de 0 até 20 de 3 em 3
print("Exemplo 4 - Contando de 0 até 20 de 3 em 3")
for i in range(0, 21, 3):
    print(i)
