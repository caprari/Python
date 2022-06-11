import cpf_generator.CPF

print('='*29)
print('* Início do Programa')
print('* Gerador de CPF')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*29)
print(' ')

from cpf_generator import CPF

cpf = CPF.generate()
formatedCpf = CPF.format(cpf)
print('CPF:', cpf)
print('CPF formatado:', formatedCpf)



# import emoji
# print(emoji.emojize("Sorriso :sunglasses:", use_aliases=True))


print(' ')
print('='*26)
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*26)
