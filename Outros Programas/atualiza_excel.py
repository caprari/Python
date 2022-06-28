import pandas as pd

tabela = pd.read_excel('Produtos.xlsx')
vendas_df = pd.DataFrame(tabela)

# print(tabela) #print de toda a tabela
# print(tabela.head(4)) #print dos 4 primeiros registros

print(vendas_df) #toda a tabela
print()

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

tabela.loc[tabela['Tipo'] == 'Produto', 'Multiplicador'] = 1.4
tabela['Preço Atualizado'] = tabela['Multiplicador'] * tabela['Preço Base Original']
vendas_df.to_excel('Produtos_pandas.xlsx', index=False)
