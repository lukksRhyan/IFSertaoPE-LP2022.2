from random import randrange, shuffle
#Jogo de adivinhar a palavra embaralhada
palavras = ["computador", "transporte", "celular", "cachorro", "edificio", "filha", "academia", "entretenimento"]

sorteada = palavras[randrange(0,len(palavras))]

saida = list(sorteada)

print("Qual palavra é essa?\n")
print("    ".join(shuffle(saida)))
acertou = False 
for i in range(3):
    entrada = input()
    if entrada == sorteada:
        acertou = True
        break
    else:
        entrada = input("Errou, tente novamente. ")

print("Parabéns, você acertou!") if acertou else print(f"Você perdeu...\n{sorteada} era a palavra correta.")
