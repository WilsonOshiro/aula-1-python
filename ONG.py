"""
Um funcionário da ONG do exercício anterior realiza o trabalho de buscar alimentos diariamente no Mercado
Municipal utilizando um carro.
É importante que a ONG saiba quantos quilômetros por litro esse carro faz.
Crie um programa em que o usuário digite quantos quilômetros o painel do carro mostra no início de uma
viagem, quantos quilômetros ele mostra na chegada ao posto de gasolina e quantos litros foram
reabastecidos. O programa deve calcular e exibir a média de quilômetros por litro que o veículo faz.

"""
print("\t\tConsumo médio de combustível\n")
"""entradas de dados no sistema"""
kmInicioViagem = float(input("Kilometragem inicial: "))
kmNoPosto = float(input("Kilometragem no posto de combustível: "))
litrosAbastecidos = float(input("Litros abastecidos: "))
"""operações"""
kmRodados = kmNoPosto - kmInicioViagem
mediaKmPorLitro = kmRodados / litrosAbastecidos
"""resultado(saída)"""
print("O veículo fez uma média de: {:.2f} Km por litro de combustível" .format(mediaKmPorLitro))
