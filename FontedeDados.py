import pandas as pd
import re


import pandas as pd
import re

#Pega a base de dados do caminho e escolher quais colunas deseja ler
tabela = pd.read_csv('ArquivosEssenciais/AllStudentsExport.csv', encoding='latin-1', sep=';', usecols=['Nome', 'Número para Msg Text'])

#Renomeia o nome das colunas
tabela.rename(columns={'Nome':'Alunos', 'Número para Msg Text':'Número'}, inplace=True)

#Deixar só o primeiro nome
n = tabela['Alunos']
colunaalunos = [n.split(' ')[0] for n in n]
###

#Atualizar coluna alunos só com o primeiro nome
tabela['Alunos'] = pd.DataFrame({'Nome':colunaalunos})


#Colocando a tabela em ordem alfabetica
tabela = tabela.sort_values('Alunos')

##Tira todos os campos vazios da tabela
tabela.dropna(inplace=True)


tabela.to_excel("ArquivosEssenciais/BancoDeDados.xlsx",index=False)
