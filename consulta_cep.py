import requests
import json

class ConsultaCep:
    @staticmethod
    def rotas(*ceps):
        dados = []
        for cep in ceps:
            url = f'https://viacep.com.br/ws/{cep}/json/'
            resposta = requests.get(url)
            dados.append(resposta.json())
        return dados

if __name__ == '__main__': 
    ceps = ['01153000', '94065200']
    dados = ConsultaCep.rotas(*ceps)
    for dado in dados:
        print(dado)