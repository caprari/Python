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

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)

# Filmes
vingadores = Filme('vingadores - guerra infinita', 2018, 160)
hulk = Filme('hulk', 2010, 100)
minions = Filme('minions 2 - a origem do gru', 2022, 120)

# Séries
atlanta = Serie('atlanta', 2018, 2)
csi = Serie('csi', 1999, 4)
terminator = Serie('terminator', 1980, 3)

# Likes
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

hulk.dar_likes()
hulk.dar_likes()
hulk.dar_likes()
hulk.dar_likes()

minions.dar_likes()
minions.dar_likes()

atlanta.dar_likes()
atlanta.dar_likes()

csi.dar_likes()
csi.dar_likes()
csi.dar_likes()
csi.dar_likes()

terminator.dar_likes()

filmes_e_series = [vingadores, hulk, minions, atlanta, csi, terminator]
playlist_fim_de_semana = Playlist('playlist_fim_de_semana', filmes_e_series)

for programa in playlist_fim_de_semana:
    print(programa)

print(f'O tamanho da lista é : {len(playlist_fim_de_semana)}')
if minions in playlist_fim_de_semana:
    print('Minions está na lista.')
else:
    print('Minions não está na lista.')

    # detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporada
    # if hasattr(programa, 'duracao'):
    #     detalhes = programa.duracao
    # else:
    #     detalhes = programa.temporada
    # print(f'Nome: {programa.nome} - {detalhes} - Likes: {programa.likes}')
    # programa.imprime()

# print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} '
#       f'- Duração: {vingadores.duracao} minutos '
#       f'- Likes: {vingadores.likes}')
# print(f'Nome: {vingadores.nome} - Likes: {vingadores.likes}')
# print(f'O filme {vingadores.nome} foi lançado em {vingadores.ano}'
#       f' e tem duração de {vingadores.duracao} minutos.')

# print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} '
#       f'- Temporadas: {atlanta.temporada} '
#       f'- Likes: {atlanta.likes}')
# print(f'Nome: {atlanta.nome} - Likes: {atlanta.likes}')






