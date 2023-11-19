#classe pai - herança

class Programa:
    def __init__(self, nome, ano, likes):
        self._nome = nome.title()
        self.ano = ano
        self._likes = likes


    def __eq__(self, other):
        return self._nome == other._nome

    @property
    def likes(self):
        return self._likes

    @likes.setter
    def likes(self, cont_likes):
        self._likes = cont_likes

    def _dar_likes(self):
        self._likes += 1

    def ver_atributos(self):
        print(" Nome:{}\n Ano:{} \n Likes:{}". format(self._nome, self.ano, self._likes))

    def __str__(self):
        return "NOME:{} - ANO:{} - LIKES:{}". format(self._nome, self.ano, self._likes)

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)



class Filme(Programa):
    def __init__(self, nome, ano, duracao, likes):
        super().__init__(nome, ano, likes)
        self.duracao = duracao

    def __str__(self):
        return "NOME:{} - ANO:{} - DURAÇÃO: {} min LIKES:{}".format(self._nome, self.duracao, self.ano, self._likes)


class Documentario(Programa):
    def __init__(self, nome, ano, duracao, likes):
        super().__init__(nome, ano, likes)
        self.duracao = duracao

    def __str__(self):
        return "NOME:{} - ANO:{} - DURAÇÃO: {} min LIKES:{}".format(self._nome, self.ano, self.duracao, self._likes)


class Serie(Programa):
    def __init__(self, nome, ano, temporadas, likes):
        super().__init__(nome, ano, likes)
        self.temporadas = temporadas

    def __str__(self):
        return "NOME:{} - ANO:{} - TEMPORADAS: {} Temporadas LIKES:{}".format(self._nome, self.ano, self.temporadas, self._likes)


class Anime(Programa):
    def __init__(self, nome, ano, episodios, likes):
        super().__init__(nome, ano, likes)
        self.episodios = episodios

    def __str__(self):
        return "NOME:{} - ANO:{} - EPISÓDIOS: {} - LIKES:{}".format(self._nome, self.ano, self.episodios,
                                                                             self._likes)

one_piece = Anime("one piece", 1999, 1076, 10)
piratas_do_caribe = Filme("piratas do caribe", 2004, 160, 5)
piratas_do_caribe2 = Filme("piratas do caribe 2", 2004, 160, 5)
lupin = Serie("lupin", 2020, 3, 1)
deuses = Documentario("eram os deuses astronautas",2010,180,3)

animes = [one_piece]

thiago_playlist = Playlist("Playlist do Thiago", animes)

print("Tamanho da Playlist: {}".format(thiago_playlist.tamanho))

for programa in thiago_playlist:
    print(programa)

print(piratas_do_caribe == piratas_do_caribe2)
