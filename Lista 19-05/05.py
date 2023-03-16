agenda = {}
#Uma agenda telefonica 'funcional'
while True:
    print(
    """
    1)Adicionar contato
    2)Adicionar número ao contato
    3)Excluir número do contato
    4)Excluir contato
    5)buscar contato
    0)Sair da agenda
    """)
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Insira o nome: ")
        numero = []
        numero.append(input("Insira o número: "))
        agenda.update({nome: numero})

    if opcao == 2:
        nome = input("Qual o nome do contato? ")
        if nome in agenda:
            agenda[nome].append(int(input("Insira o número: ")))
        else:
            print("Não existe nenhum contato com esse nome.")

    if opcao == 3:
        nome = input("Qual o número do contato? ")
        i=1
        if nome in agenda:
            if len(agenda[nome]) == 1:
                agenda.pop(nome)
            else:
                print("Escolha um número para remover: ")
                print(nome+':\n')
                for numero in agenda[nome]:
                    print(f"{i}-{numero}\n")
                    i +=1
                numApagado = int(input())
                agenda[nome].pop(numApagado-1)
    if opcao == 4:
        nome = input("Qual o número do contato? ")
        if nome in agenda:
            agenda.pop(nome)
    if opcao == 5:
        nome = input("Insira o nome do contato: ")
        if nome in agenda:
            print(f"\n{nome}:\n")
            i=1
            for numero in agenda[nome]:
                print(f"{i}-{numero}")
                i += 1
        else:
            print("Contato não encontrado.")
    if opcao == 0:
        break