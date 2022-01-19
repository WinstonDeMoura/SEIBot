
########################## ZapBot #########################################
## Código feito para uso interno na empresa, com uma base de dados -    ##
## relativamente pequena.                                              ##
### Não recomendo o uso para Marketing. Seu Número pode ser bloqueado ###
############# Me insento de qualquer responsabilidade ###################


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import urllib


#Abre o Chrome
options = webdriver.ChromeOptions()
navegador = webdriver.Chrome(ChromeDriverManager().install(), options=options)
site = ("https://web.whatsapp.com")
navegador.get(site)

#Enquanto ele não faz o login o código não executa
while len(navegador.find_elements(By.ID,"side")) < 1:
  time.sleep(1)

#Código para fechar o whatsapp Web e desconectar do computador
navegador.find_element(By.XPATH,'//*[@id="side"]/header/div[2]/div/span/div[3]/div/span').click()
time.sleep(6)
navegador.find_element(By.XPATH,'//*[@aria-label="Desconectar"]').click()
time.sleep(10)

navegador.close()