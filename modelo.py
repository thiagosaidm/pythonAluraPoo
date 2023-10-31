
class Filme:
    def __init__(self, nome, ano, duracao, likes):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = likes

    @property
    def likes(self):
        return self.__likes

    @likes.setter
    def likes(self, cont_likes):
        self.__likes = cont_likes

    def _dar_likes(self):
        self.__likes += 1

    def ver_atributos(self):
        print(" Nome:{}\n Ano:{} \n Duração:{} \n Likes:{}". format(self.__nome, self.ano, self.duracao, self.__likes))

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas




