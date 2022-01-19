
########################## ZapBot #########################################
## Código feito para uso interno na empresa, com uma base de dados -    ##
## relativamente pequena.                                              ##
### Não recomendo o uso para Marketing. Seu Número pode ser bloqueado ###
############# Me insento de qualquer responsabilidade ###################

import pandas as pd

#Acessa o banco de dados do Execel
alunos_df = pd.read_excel('ArquivosEssenciais\BancoDeDados.xlsx')


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import urllib

#Define a mensagem padrão a ser enviada
mensagem = input("Digite seu texto: ")
print(mensagem)
time.sleep(10)

#Abre o Chrome
options = webdriver.ChromeOptions()
navegador = webdriver.Chrome(ChromeDriverManager().install(), options=options)
site = ("https://web.whatsapp.com")
navegador.get(site)

#Enquanto ele não faz o login o código não executa
while len(navegador.find_elements(By.ID,"side")) < 1:
  time.sleep(1)

#Acessa a base de dados e coloca nó código para ser enviado
for i, aluno in enumerate(alunos_df['Aluno']):
  numero = alunos_df.loc[i, "Número"]
  texto = urllib.parse.quote(f"Oi {aluno}! {mensagem}")
  link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
  navegador.get(link)
  time.sleep(10)
  navegador.find_element(By.XPATH,"//span[@data-icon='send']").click()
  time.sleep(5)
  #Código para fechar o whatsapp Web e desconectar do computador
navegador.find_element(By.XPATH,'//*[@id="side"]/header/div[2]/div/span/div[3]/div/span').click()
time.sleep(6)
navegador.find_element(By.XPATH,'//*[@aria-label="Desconectar"]').click()
time.sleep(10)

navegador.close()