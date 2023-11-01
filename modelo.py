#classe pai - herança

class Programa:
    def __init__(self, nome, ano, likes):
        self._nome = nome.title()
        self.ano = ano
        self._likes = likes

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
lupin = Serie("lupin", 2020, 3, 1)
deuses = Documentario("eram os deuses astronautas",2010,180,3)

playlist = [lupin, piratas_do_caribe, one_piece, deuses]

for programa in playlist:
    print(programa)