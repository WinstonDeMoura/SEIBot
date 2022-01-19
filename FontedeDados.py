import pandas as pd
import re



tabela = pd.read_csv('Downloads/TRASH/AllStudentsExport.csv', encoding='latin-1', sep=';', usecols=['Nome', 'Número para Msg Text'])
tabela.rename(columns={'Nome':'Alunos', 'Número para Msg Text':'Número'}, inplace=True)
##Tira todos os campos vazios da tabela
tabela.dropna(inplace=True)

n = tabela.columns('Nome')
print(n)

