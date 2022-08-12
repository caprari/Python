class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa..')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa Caelumer.')

    def busca_curso_do_mes(self, mes=None):
        print(f'Mostrando cursos do {mes}' if mes else 'Monstrando cursos desse mês')


class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa Alurar')

    def busca_pergunta_sem_resposta(self):
        print('Mostrando perguntas não respondidas.')


class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'

class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass

class Senior(Alura, Caelum, Hipster):
    pass

luan = Senior('luan')
print(luan)




