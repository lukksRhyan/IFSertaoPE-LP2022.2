import requests
#Api de casos de covid 19 A chave que tá ai não sei se pode ser reutilizada.
"""
Variáveis que seriam usadas com a API do Brasil.io, caso ela estivesse disponível.
BRIIO_URl = f"https://api.brasil.io/v1/dataset/covid19/caso/data/?is_last=True&place_type=state"
BRIO_KEY = "314de0cdea9de763fe22b3cf383c27d97d0988f4"
BRIO_KEY2 = "ef140a63a2dbdb4a54f09665c0a0fd3b8cd25b1f"
"""
COVBR_URL = "https://covid19-brazil-api.vercel.app/api/report/v1/brazil/"

UF = input("Digite a sigla do estado do qual você quer saber o número de casos\n").upper()
data = input("Digite a  data a ser pesquisada no formato AAAA MM DD (A = Ano, M = Mês, D = Dia)\n")
data_pURL = data.replace(" ", "")

COVBR_URL += data_pURL

resposta = requests.get(COVBR_URL)
info = resposta.json()

for estado in info['data']:
    if estado['uf'] == UF:
        print(f"\n{estado['state']}, dia {data}:\n")
        print(f"Número de casos: {estado['cases']}\nNúmero de mortes: {estado['deaths']}\n")