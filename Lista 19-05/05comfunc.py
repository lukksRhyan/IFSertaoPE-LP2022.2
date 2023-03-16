def busca(dicionario = dict()):
    nome = input("Insira o nome do contato: ")
    if nome in dicionario:return True
    else: return False


def adicionar(contato,agenda, *numero):
    agenda[contato].append(numero)

contatos = dict({})
#mesma da ultima so que com funcoes
while True:
    print(
    """
    1)Adicionar contato
    2)Adicionar número ao contato
    3)Excluir número do contato
    4)Excluir contato
    5)buscar contato
    """)
    opcao = int(input("Escolha uma opção"))

    if opcao == 1:
        nome = busca(contatos)
        

    if opcao == 2:
        if busca(contatos):
            contatos[nome].append(int(input("Insira o número: ")))
        else:
            print("Não existe nenhum contato com esse nome.")

    if opcao == 3:
        nome = input("Qual o número do contato? ")
        i=1
        if nome in contatos:
            if len(contatos[nome]) == 1:
                contatos.pop(nome)
            else:
                print("Escolha um número para remover: ")
                print(nome+':\n')
                for numero in contatos[nome]:
                    print(f"{i}-{numero}\n")
                    i +=1
                numApagado = int(input())
                contatos[nome].pop(numApagado-1)
    if opcao == 4:
        nome = input("Qual o número do contato? ")
        if not nome in contatos:
            print("Contato não encontrado.")
        else:
            contatos.pop(nome)
    if opcao == 5:
        nome = busca(contatos)
        if nome == False:
            print("Contato não encontrado.")
        else:
            i=1
            for numero in contatos[nome]:
                print(i+'-'+numero)