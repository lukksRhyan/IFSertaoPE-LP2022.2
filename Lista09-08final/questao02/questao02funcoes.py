from xmlrpc.client import MAXINT, MININT
import requests
import json
#Funcionamento da api de acoes
def valorizacao(stock, dias_uteis):

    link = "https://api-cotacao-b3.labdo.it/api/cotacao/cd_acao/"+stock
    answer = requests.get(link).text
    market = json.loads(answer)
    old_value = market[dias_uteis]['vl_minimo']

    new_value = market[0]['vl_minimo']
    
    diff = ((new_value/old_value) - 1) * 100

    return(diff)

def ver_ticker():
    cod = input("Insira o código da ação a ser vista: ")
    
    with open('tickers.json', 'r') as arqv:
        acoes = json.load(arqv)
        print("nome da empresa: " + acoes['data'][cod.upper()])

    link = "https://api-cotacao-b3.labdo.it/api/cotacao/cd_acao/"+ cod
    answer = requests.get(link).text
    market = json.loads(answer)

    valor = market[0]['vl_minimo']
    diferenca = round(valorizacao(cod, 45), 3)
    print(f"Valendo atualmente: {valor}\nValorização de: {diferenca}%")
    cont = input("Aperte enter para prosseguir")

def att_ticker():

    cod = input("Insira o código da empresa a ser cadastrada: ").upper()
    
    with open('tickers.json', 'r') as arqv:
        tickers = json.load(arqv)

    link = "https://api-cotacao-b3.labdo.it/api/cotacao/cd_acao/" + cod
    answer = requests.get(link).text

    nome = json.loads(answer)[0]['nm_empresa_rdz']
    print(nome)
    stock = {f"{cod}" : nome}
    tickers['data'].update(stock)

    with open('tickers.json', 'w') as arqv:
        arqv.write(json.dumps(tickers))
    cont = input("Aperte enter para prosseguir")

def del_ticker():
    with open("tickers.json") as arqv:
        ticker = json.load(arqv)

    while True:
        cod = input("Insira o código da ação a ser excluída: ")
        res = input(f"A ação que você planeja excluir é a {ticker[cod.upper()]}? s/n \n")
        if res == 's':
            ticker['data'].pop(cod.upper())
            break
    
    with open('tickers.json', 'w') as arqv:
        arqv.write(json.dumps(ticker))
        
def todas_acoes():
    with open('tickers.json', 'r') as arqv:
        ticker = json.load(arqv)['data']
    maior = MININT
    menor = MAXINT
    acao_maior = str()
    acao_menor = str()
    for acao in ticker:
        rent = valorizacao(acao, 45)
        print(acao + " " + str(round(rent, 2)))
        if rent > maior:
            acao_maior = acao
            maior = rent
        elif rent < menor:
            acao_menor = acao
            menor = rent
    print(f'acao mais valorizada {acao_maior} com {round(maior, 3)}%\nacao mais desvalorizada {acao_menor} com {round(menor, 3)}%')
    cont = input("Aperte enter para prosseguir")