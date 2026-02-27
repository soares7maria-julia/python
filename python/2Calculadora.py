#CALCULADORA DE JUROS COMPOSTOS

inicial = int(input("Valor Inicial: "))
taxa = float(input("Valor da taxa mensal em decimal: "))
tempo_desejado = int(input("Tempo em meses: "))
salario_desejado = int(input("salário mensal que você quer receber ao se aposentar: "))
aporte = int(input("Quanto dinheiro voce consegue aportar por mes: "))

''''''

tempo_decorrido = 0
while tempo_decorrido < tempo_desejado:
      
      if tempo_decorrido == 0:
            montante = round(inicial * (1 + taxa) ** tempo_desejado, 2)
            tempo_decorrido = tempo_decorrido + 1

      else:
            montante = round((inicial + aporte) * (1 + taxa) ** tempo_desejado, 2) 
            tempo_decorrido = tempo_decorrido + 1

print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")

print(f"Seu Valor final será de {montante}.")

salario_mensal = round((montante * taxa)/12, 2)

if salario_mensal >= salario_desejado:
    print(f"Parabens você já pode se aposentar, pois seu salario será de {salario_mensal}")

else: 
        print(f"Você ainda não alcançou o salario desejado, pois o seu salario será de {salario_mensal}")

