class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    # def imprime(self):
    #     print(f'{self._nome} - {self.ano} - {self._likes} likes')
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} likes'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    # def imprime(self):
    #     print(f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} likes')
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada

    # def imprime(self):
    #     print(f'{self._nome} - {self.ano} - {self.temporada} temporadas - {self._likes} likes')
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporada} temporadas - {self._likes} likes'


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_likes()
# print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} '
#       f'- Duração: {vingadores.duracao} minutos '
#       f'- Likes: {vingadores.likes}')
# print(f'Nome: {vingadores.nome} - Likes: {vingadores.likes}')
# print(f'O filme {vingadores.nome} foi lançado em {vingadores.ano}'
#       f' e tem duração de {vingadores.duracao} minutos.')

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_likes()
atlanta.dar_likes()
# print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} '
#       f'- Temporadas: {atlanta.temporada} '
#       f'- Likes: {atlanta.likes}')
# print(f'Nome: {atlanta.nome} - Likes: {atlanta.likes}')

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    # detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporada
    # if hasattr(programa, 'duracao'):
    #     detalhes = programa.duracao
    # else:
    #     detalhes = programa.temporada
    # print(f'Nome: {programa.nome} - {detalhes} - Likes: {programa.likes}')
    # programa.imprime()
    print(programa)




