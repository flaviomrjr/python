from ExtratorArgumentosUrl import ExtratorArgumentosUrl
#argumento = "moedaorigem=real"
#USANDO FIND PARA DEFINIR INDEX
#index = argumento.find("=")
#CRIANDO SUBSTRING A PARTIR DO INDEX + 1
#substring = argumento[index + 1:]
#print(substring)

#CRIANDO UM VETOR, FAZENDO SEPARAÇAO DE PALAVRA A PARTIR DO =
#listaargumentos = argumento.split("=")
#print((listaargumentos))

url = "https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar"
argumentosUrl = ExtratorArgumentosUrl(url)
argumentosUr2 = ExtratorArgumentosUrl(url)
moedaOrigem, moedaDestino = argumentosUrl.extraiArgumentos()
print(moedaDestino,moedaOrigem)
#print(ExtratorArgumentosUrl.urlEhValida(url))

#string = "bytebank"
#stringNova = string.replace("byte","rodrigo",1)
#print(stringNova)

#urlByteBank = "https://byteback.com"

#COMPARANDO INSTANCIAS
print(argumentosUrl==argumentosUr2)
