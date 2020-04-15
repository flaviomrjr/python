class ExtratorArgumentosUrl:
    def __init__(self,url):
        #VERIFICA SE A URL É VALIDA
        if self.urlEhValida(url):
            self.url = url
        else:
            raise LookupError("Url inválida")

    def __eq__(self, outraInstancia):
        return self.url == outraInstancia.url

    #MÉTODO STATICO, NÃO MUDA, NÃO USAMOS O SELF
    @staticmethod
    def urlEhValida(url):
        if url and url.startswith("https://bytebank.com"):
            return True
        else:
            return False

    def extraiArgumentos(self):

        buscaMoedaOrigem = "moedaorigem"
        buscaMoedaDestino = "moedadestino"

        #FAZ A BUSCA DO INDEX UTILIZANDO O FIND MAIS O LEN
        indiceInicialMoedaDestino = self.encontraIndiceInicial(buscaMoedaDestino)

        indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
        indiceFinalMoedaOrigem = self.url.find("&")


        moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]

        if moedaOrigem == "moedadestino":
            self.trocaMoedaOrigem()

        moedaDestino = self.url[indiceInicialMoedaDestino:]

        return moedaOrigem,moedaDestino

    #METODO PARA BUSCAR INDECE NA URL
    def encontraIndiceInicial(self,moedaBuscada):
        return self.url.find(moedaBuscada) + len(moedaBuscada) + 1

    #REPLACE DE STRING
    def trocaMoedaOrigem(self):
        self.url = self.url.replace("moedadestino","real",1)
        print(self.url)

