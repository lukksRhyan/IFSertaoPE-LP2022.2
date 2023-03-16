import json

def atualizarCTT():
    
    novoContato = input("insira o nome do contato: ")
    with open("Contatos.json", 'r') as lista:
        contatos = json.load(lista)

    for pessoa in contatos:
        if pessoa['nome'] == novoContato:
            print("Contado já na lista.\n")
        else:
            numero = input("Insira o número do novo contato: ")
            contato = {
                'nome': novoContato,
                'numero': numero 
            }
            contatos.append(contato)
    with open("Contatos.json", 'w') as lista:
        json.dump(contatos, lista)

def removerCTT():

    with open("contatos.json", 'r') as list:
        contatos = json.load(list)

    nome = input("Insira o contato a ser excluido: ").upper()
    for pessoa in contatos:
        if pessoa['nome'].upper() == nome:
            contatos.remove(pessoa)

#atualizarCTT()