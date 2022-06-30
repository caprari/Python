import pandas as pd

tabela = pd.read_excel('Produtos_pandas.xlsx')
vendas_df = pd.DataFrame(tabela)

# print(tabela) #print de toda a tabela
# print(tabela.head(4)) #print dos 4 primeiros registros

# print(vendas_df) #toda a tabela
# print()

# print(vendas_df.head(4)) #exibir qtde de registros
# print()
#
# print(vendas_df.shape) #exibir qtde de linhas e colunas
# print()
#
# print(vendas_df.describe()) #descrição dos campos, resumo
# print()
#
# produtos = vendas_df['Produtos'] #exibe apenas a coluna Produtos
# print(produtos)

# print(vendas_df.loc[2:4]) #exibe os registros das linhas 2 até 4

# vendas_produto_df = vendas_df.loc[vendas_df['Tipo'] == 'Produto'] #exibe apenas os registros do Tipo Produto
# print(vendas_produto_df)
#
# vendas_servico_df = vendas_df.loc[vendas_df['Tipo'] == 'Serviço'] #exibe apenas os registros do Tipo Serviço
# print(vendas_servico_df)

# vendas_servico_df_resumo = vendas_df.loc[vendas_df['Tipo'] == 'Produto',
#                                          ['Produtos', 'Preço Atualizado']]
# exibe apenas os registros do Tipo Produto e as colunas Produtos e Preço Atualizado
#vendas_df.loc[linhas, colunas]
# vendas_servico_df_resumo = vendas_df.loc[vendas_df['Tipo'] ==
#                                          'Produto', ['Produtos', 'Preço Atualizado']]

# print(vendas_servico_df_resumo)
# atualizar um campo da coluna
# tabela.loc[tabela['Tipo'] == 'Produto', 'Multiplicador'] = 1.4
# tabela['Preço Atualizado'] = tabela['Multiplicador'] * tabela['Preço Base Original']
# gravar novo arquivo excel
# vendas_df.to_excel('Produtos_pandas.xlsx', index=False)

#criar nova coluna
# vendas_df['Comissão'] = vendas_df['Preço Atualizado'] * 0.05
# vendas_df.loc[:, 'Imposto'] = 1

#excluir colunas
# vendas_df = vendas_df.drop('Preço Atualizado', axis=1)
# vendas_df = vendas_df.drop(0, axis=0)

# deletar linhas completamente vazias
# vendas_df = vendas_df.dropna(how='all', axis=1)

# deletar linhas que possuem algum registro vazio
# vendas_df = vendas_df.dropna()

# preencher valores vazios com 1
# vendas_df['Comissão'] = vendas_df['Comissão'].fillna(1)

# preencher valores vazios com media
# vendas_df['Comissão'] = vendas_df['Comissão'].fillna(vendas_df['Comissão'].mean())

# preencher com o ultimo valor acima caso esteja vazio
# vendas_df = vendas_df.ffill()

# soma a quantidade de linhas conforme o parâmetro
# tipo = vendas_df['Tipo'].value_counts()
# print(tipo)

# agrupar os valores conforme a coluna
# faturamento = vendas_df.groupby('Tipo').sum()
# print(faturamento)

# agrupar os valores conforme a coluna e mostrar apenas algumas colunas
# faturamento2 = vendas_df[['Tipo', 'Preço Base Original', 'Preço Atualizado']].groupby('Tipo').sum()
# print(faturamento2)

responsavel = pd.read_excel('Responsavel_pandas.xlsx')
vendas_df = vendas_df.merge(responsavel)



print(vendas_df)
vendas_df.to_excel('Produtos_pandas.xlsx', index=False)

