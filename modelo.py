#classe pai - herança

class Programa:
    def __init__(self, nome, ano, likes):
        self._nome = nome.title()
        self.ano = ano
        self._likes = likes

    @property
    def likes(self):
        return self.__likes

    @likes.setter
    def likes(self, cont_likes):
        self._likes = cont_likes

    def _dar_likes(self):
        self._likes += 1

    def ver_atributos(self):
        print(" Nome:{}\n Ano:{} \n Likes:{}". format(self._nome, self.ano, self._likes))


class Filme(Programa):
    def __init__(self, nome, ano, duracao, likes):
        super().__init__(nome, ano, likes)
        self.duracao = duracao


class Serie(Programa):
    def __init__(self, nome, ano, temporadas, likes):
        super().__init__(nome, ano, likes)
        self.temporadas = temporadas




