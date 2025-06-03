import requests

# #url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
# url= "https://economia.awesomeapi.com.br/json/daily/USD-BRL/15"
# resposta = requests.get(url)
#
# # Verifica se a requisição foi bem-sucedida (código 200)
# if resposta.status_code == 200:
#     dados = resposta.json()
#     print(dados)
# else:
#     print(f"Erro na requisição: {resposta.status_code}")
#

def cotacao_euro():
    url = "https://economia.awesomeapi.com.br/json/daily/EUR-BRL"
    resposta = requests.get(url)

    # Verifica se a requisição foi bem-sucedida (código 200)
    if resposta.status_code == 200:
        dados = resposta.json()
        bid = dados[0]["bid"]
        print(f"Cotação atual do Euro: R$ {float(bid):.2f}")
    else:
        print(f"Erro na requisição: {resposta.status_code}")

def cotacao_dolar():
    url = "https://economia.awesomeapi.com.br/json/daily/USD-BRL"
    resposta = requests.get(url)

    # Verifica se a requisição foi bem-sucedida (código 200)
    if resposta.status_code == 200:
        dados = resposta.json()
        bid = dados[0]["bid"]
        print(f"Cotação atual do Euro: R$ {float(bid):.2f}")
    else:
        print(f"Erro na requisição: {resposta.status_code}")



def cotacao_moeda(abreviacao, moeda):
    url = f"https://economia.awesomeapi.com.br/json/daily/{abreviacao}-BRL"
    resposta = requests.get(url)

    # Verifica se a requisição foi bem-sucedida (código 200)
    if resposta.status_code == 200:
        dados = resposta.json()
        bid = dados[0]["bid"]
        print(f"Cotação atual do {moeda}: R$ {float(bid):.2f}")
    else:
        print(f"Erro na requisição: {resposta.status_code}")


def escolher_moeda():
    moeda_escolhida = input(
        '''Escolha a moeda digitando o número:
        1) USD - Dólar
        2) EUR - Euro
        3) BTC - Bitcoin
        '''
    )

    if moeda_escolhida == '1':
        return 'USD', 'Dólar'
    elif moeda_escolhida == '2':
        return 'EUR', 'Euro'
    elif moeda_escolhida == '3':
        return 'BTC', 'Bitcoin'


abreviacao_, moeda_ = escolher_moeda()

cotacao_moeda(abreviacao_, moeda_)