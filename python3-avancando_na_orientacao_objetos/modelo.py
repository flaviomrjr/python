#CRIANDO CLASSE PROGRAMA
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    #DEFININDO PROPERTY LIKES
    @property
    def likes(self):
        return self._likes

    #DEFININDO METODO DAR LIKE
    def dar_like(self):
        self._likes += 1

    #DEFININDO PROPERT NOME
    @property
    def nome(self):
        return self._nome

    #DEFININDO SETTER PARA ALTERAR NOME
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    #DEFININDO STR PARA EXECUTAR O PRINT
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes'

#CRIANDO CLASSE FILME E HERANÇA DA CLASSE PROGRAMA
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        #CHAMADNO ATRIBUTOS DA CLASSE PAI
        super().__init__(nome, ano)
        #DEFININDO ATRIBUTOS DA CLASE FILME
        self.duracao = duracao

    #DEFININDO PRINT DA CLASSE FILME
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao}  min - {self._likes} Likes'

#CRIANDO CLASSE SERIE E HERANÇA DA CLASSE PROGRAMA
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas}  temporadas - {self._likes} Likes'

#CRIA CLASSE PLAYLIST
class PLaylist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    #ADCIONANDO UM ITEM EM PROGRAMA PARA DEIXA A PLAYLIST INTERAVEL habilitando for in = DUCK TYPING
    def __getitem__(self, item):
        return self._programas[item]

    #CRIANDO PROPERTY PARA EXIBIR PROGRAMAS PARA NAO ACESSAR A VARIABEL COM _
    @property
    def listagem(self):
        return self._programas

    #DEIXANDO PLAYLIST COMO SIZED PARA PODER USAR O LEN = DUCK TYPING
    def __len__(self):
        return len(self._programas)
    #USAMOS O ATRIBUTO PROGRAMAS POIS ELE ARMAZENA OS ITEM DA PLAYLIST (LISTA)

#DEFININDO FILMES E SERIES
vingadores = Filme('vingadores - guerra infinita','2018','160')
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('todo mundo em panico', 1999, 100)
demolidor = Serie('Demolidor', 2018, 3)

#ATRIBUINDO LIKES
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()

#CRIANDO LISTA COM OS FILMES E SERIES
filmes_e_series = [vingadores, atlanta, demolidor, tmep]

#CRIANDO PLAYLIST COM DADOS DA LISTA FILMES E SERIES
playlist_fim_de_semana = PLaylist('fim de semana', filmes_e_series)

#VERIFICANDO TAMANHO DA PLAYLIST
print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')

#EXIBINDO DADOS DA PLAYLIST
for programa in playlist_fim_de_semana:
    print(programa)

#VERIFICANDO SE A SERIE DEMOLIDOR ESTA NA PLAYLIST
print(f'Ta ou nao ta? {demolidor in playlist_fim_de_semana}')

#EXIBINDO APENAS O PRIMEIRO ITEM DA PLAYLIST
print(playlist_fim_de_semana[0])