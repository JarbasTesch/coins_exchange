print('atualizando o git')

'''
Precisa criar a venv!!!!
'''

import requests

url = "https://api.exemplo.com/dados"
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida (código 200)
if response.status_code == 200:
    dados = response.json()  # Converte a resposta para dicionário Python
    print(dados)
else:
    print(f"Erro na requisição: {response.status_code}")
