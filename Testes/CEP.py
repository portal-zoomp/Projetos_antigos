import requests

cep = input('Informe CEP: ')
url = f'http://viacep.com.br/ws/{cep}/json'
try:
    endereco = requests.get(url).json()
except:
    print('CEP Inválido')
try:
    print(f"""CEP: {endereco["cep"]}\nLogradouro: {endereco["logradouro"]}\nComplemento: {endereco["complemento"]}
Bairro: {endereco["bairro"]}\nCidade: {endereco["localidade"]}\nUF: {endereco["uf"]}\nDDD: {endereco["ddd"]}""")
except:
    print('CEP não encontrado')
