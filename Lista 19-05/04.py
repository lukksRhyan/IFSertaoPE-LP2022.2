#Recebe dados de voltas de corrida e compara os tempos dos pilotos
tabelaTempos = {
    "Verstapen": [],
    "Perez": [],
    "Russel": [],
    "Sainz": [],
    "Hamilton": [],
    "Bottas": [],
    }
    
for corredor in tabelaTempos:
    for i in range(3):
        tempoCorrida = float(input(f"Insira o tempor da volta {i+1} do corredor {corredor}\n"))
        tabelaTempos[corredor].append(tempoCorrida)
print(tabelaTempos)

menorTempo = 350
for corredor,tempos in tabelaTempos.items():
    for volta in tempos:
        if volta < menorTempo:
            menorTempo = volta
            melhorCorredor = corredor
            melhorVolta = tabelaTempos[corredor].index(volta) + 1

for corredor, tempo in tabelaTempos.items():
    print(corredor +":")
    for volta in tempo:
        print(f"-{volta}    ")
    print("\n")

print(f"O melhor corredor foi {melhorCorredor}, com {menorTempo} segundos na volta {melhorVolta}.")