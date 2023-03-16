from questao02funcoes import todas_acoes, ver_ticker, att_ticker, del_ticker

while True:

    print("\n\nSistemas de cadastros de acoes.\n")

    opcao = int(input("Escolha a opção:\n 1)Ver uma ação cadastrada\n 2)adcionar uma nova ação\n 3)Excluir uma ação cadastrada\n 4)Ver ações mais valorizadas\n 0)Sair do sistema\n\n"))
    
    if opcao == 1:
        ver_ticker()
    elif opcao == 2:
        att_ticker()
    elif opcao == 3:
        del_ticker()
    elif opcao == 4:
        todas_acoes()

    else:
        break