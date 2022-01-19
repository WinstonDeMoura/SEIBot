while True: 
  
  nome = input("Digite o nome do aluno: ")
  recupe = input("Digite o número de recuperações: ")
  print("Escolha o curso abaixo: ")
  print (" 1 - D&C")
  print (" 2 - Pérola de Grande Valor")
  print (" 3 - Preparação M")
  print (" 4 - Casamento")
  print (" 5 - ME")

  curso_entrada = int(input("Digite o numero do Curso: "))
  curso = (curso_entrada)
  if (curso_entrada == 1):
    curso = ("D&C")
  elif (curso_entrada == 2):
    curso = ("Pérola de Grande Valor")
  elif (curso_entrada == 3):
    curso = ("Preparação M")
  elif (curso_entrada == 4):
    curso = ("Casamento ")
  elif (curso_entrada == 5):
    curso = ("ME")


#Aqui definiremos o sexo do aluno para formar o texto
  print("Digite o sexo do aluno: ")
  print ("Digite 1 - Para Masculino")
  print ("Digite 2 - Para Feminino")
  se = int(input("Sexo: "))
  if (se == 1):
    se = ("do")
  else:
    se = ("da")  
#---

  numero = int(input("Digite o número de telefone com ddd: "))
  fone = (f"55{numero}") 


  link = (curso)
  if (curso == "D&C"):
    link = (" ou fazer online no seguinte link: imo.pe.hu/dec")
  elif (curso == "Pérola de Grande Valor"):
    link = ("ou fazer online no seguinte link: imo.pe.hu/perola")
  elif (curso == "Preparação M"):
    link = ("ou fazer online no seguinte link: imo.pe.hu/pm")
  elif (curso == "Casamento"):
    link = ("ou fazer online no seguinte link: imo.pe.hu/casamento")
  elif (curso == "ME"):
    link = ("ou fazer online no seguinte link: imo.pe.hu/mulheres")
  else:
    link = (".")
#-----------

#texto que será formado
  texto = (f"Olá *{nome}*! Você precisa de *{recupe}* recuperações do curso de *{curso}* para ficar aprova{se} nesse semestre. Você pode fazer as recuperações aqui na sede {link} ")
  print (texto)
#---


  import urllib3
  from urllib.parse import quote
  text = quote(texto)
  zap = ("https://api.whatsapp.com/send?phone=")
  link =(f"{zap}{fone}&text={text}")

# Link que será gerado  
  print (link)

# Escolha se Vai executar o programa novamente
  print ("1 - Executar Novamente")
  print ("2 - Sair")
  opcao = int(input("> "))
  if (opcao == 1):
    continue
  elif (opcao == 2):
    break
  else:
    print ("Opcao invalida!")