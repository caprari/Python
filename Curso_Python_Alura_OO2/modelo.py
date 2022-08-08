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


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao


class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_likes()
# print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} '
#       f'- Duração: {vingadores.duracao} minutos '
#       f'- Likes: {vingadores.likes}')
print(f'Nome: {vingadores.nome} - Likes: {vingadores.likes}')
# print(f'O filme {vingadores.nome} foi lançado em {vingadores.ano}'
#       f' e tem duração de {vingadores.duracao} minutos.')

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_likes()
atlanta.dar_likes()
# print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} '
#       f'- Temporadas: {atlanta.temporada} '
#       f'- Likes: {atlanta.likes}')
print(f'Nome: {atlanta.nome} - Likes: {atlanta.likes}')




