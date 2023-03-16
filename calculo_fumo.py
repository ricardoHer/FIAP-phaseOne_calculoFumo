# Nome: Ricardo Hernandez
# RM: 99167

# Nome: Wesley Ninaja
# RM: 98115

# Nome: Erick Gruber
# RM: 99584

# Nome: Bruno Fukumori
# RM: 99486

# Nome: João Cantalice
# RM: 550177

# ler o tempo em anos que o usuário fuma
anosFumante: float
while True:
    entrada = input("Tempo como fumante (em anos)......: ")
    if entrada.replace(".", "", 1).isdigit():
        anosFumante = float(entrada)
        break
    else:
        print("Entrada inválida! Informa apenas números positivos e/ou com decimais separados por ponto (.)")

# ler valor atual do maço
valorAtualMaco: float
while True:
    entrada = input("Valor do maço.....................: ")
    if entrada.replace(".", "", 1).isdigit():
        valorAtualMaco = float(entrada)
        break
    else:
        print("Entrada inválida! Informa apenas números positivos e/ou com decimais separados por ponto (.)")

# ler quantidade média de maços fumados por dia
qtdeMacosPorDia: int
while True:
    entrada = input("Quantidade de maços por dia.......: ")
    if entrada.replace(".", "", 1).isdigit():
        qtdeMacosPorDia = float(entrada)
        break
    else:
        print("Entrada inválida! Informa apenas números positivos e/ou com decimais separados por ponto (.)")

# efetuar o calculo de montante já gasto
# considere o mes comercial de 30 dias para fazer os cálculos
qtdeDiasMes = 30

#   meses = ano / 12
#   dias = meses / 30
#   quantidadeMacosPeriodo = dias * mediaMacos
#   valorTotalGasto = quantidadeMacosPeriodo * valorMedio
quantidadeMacosPeriodo = ((anosFumante * 12) * qtdeDiasMes) * qtdeMacosPorDia
montanteGastoAtualmente: float = quantidadeMacosPeriodo * valorAtualMaco    

# se o valor for abaixo de 20.000 escreva: "Com o valor R$ <montante>, você poderia ter dado entrada em um carro."
if montanteGastoAtualmente < 20000:
    print(f"Com o valor R$ {montanteGastoAtualmente:.2f}, você poderia ter dado entrada em um carro.")

# se o valor for entre 20.000 e 50.000 escreva:
# "Com o valor R$ <montante>, você poderia ter comprado um carro popular usado"
elif 20000 <= montanteGastoAtualmente <= 50000:
    print(f"Com o valor R$ {montanteGastoAtualmente:.2f}, você poderia ter comprado um carro popular usado.")

# se o valor for acima de 50.000 escreva: "Com o valor R$ <montante> , você poderia ter comprado um carro zero."
else:
    print(f"Com o valor R$ {montanteGastoAtualmente:.2f}, você poderia ter comprado um carro zero.")


