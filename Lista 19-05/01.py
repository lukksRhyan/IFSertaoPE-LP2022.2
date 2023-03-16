#Escreve um nome varias vezes tirando uma letra por vez
nome = input("insira seu nome: ")
for letra in nome:
    print(nome[letra:])