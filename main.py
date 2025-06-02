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

def cotacao_moeda(moeda_real):
    url = f"https://economia.awesomeapi.com.br/json/daily/{moeda_real}-BRL"
    resposta = requests.get(url)

    # Verifica se a requisição foi bem-sucedida (código 200)
    if resposta.status_code == 200:
        dados = resposta.json()
        bid = dados[0]["bid"]
        print(f"Cotação atual do Euro: R$ {float(bid):.2f}")
    else:
        print(f"Erro na requisição: {resposta.status_code}")

moeda_escolhida = input(
    '''Escolha a moeda digitando o número:
    1) USD - Dólar
    2) EUR - Euro
    3) BTC - Bitcoin
    '''
)

#FAZER O IF PRA SETAR A MOEDA

cotacao_moeda(moeda_escolhida)