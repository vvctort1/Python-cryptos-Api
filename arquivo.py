with open("cryptos_values.txt","w") as arquivo:
    arquivo.write("")


url = "https://api.api-ninjas.com/v1/cryptosymbols?"

lista = []

try: 
    response = requests.get(url, headers={"X-Api-Key": "RWg4SA2qGApINIIpaRisDQ==zay7vlJQ2kSpFBzd"})

    if response.status_code == requests.codes.ok:
        
        dicionario = response.json()

        print(dicionario)

        for key,value in dicionario.items():
            if key == "symbols":
                for moeda in value:
                    lista.append(moeda)
                

        with open("symbols_crypto.json","w") as arquivo:
            json.dump(dicionario,arquivo,indent=4)

except ConnectionError:
    print("Erro de conexao")
except Exception as erro:
    print(f"Erro: {erro}")


import requests
import json


lista_cryptos = []


for symbol in lista:

    url2 = f'https://api.api-ninjas.com/v1/cryptoprice?symbol={symbol}'.format(symbol)

    try:

        response = requests.get(url2, headers={'X-Api-Key': 'RWg4SA2qGApINIIpaRisDQ==zay7vlJQ2kSpFBzd'})

        if response.status_code == requests.codes.ok:

            dicionario = response.json()

            cryptos = {}

            cryptos["symbol"] = symbol

            for key,value in dicionario.items():
                if key == "price":
                    cryptos[key] = value
            lista_cryptos.append(cryptos)

            with open("cryptos_values.txt","a") as arquivo:
                for key,value in cryptos.items():
                    if key == "symbol":
                        arquivo.write(f"{value} : ")
                    elif key == "price":
                        arquivo.write(f"{value} \n")

            
    except ConnectionError:
        print("Erro de conexao")
    except Exception as erro:
        print(f"Erro: {erro}")