#Condicionais
# if, elif, else
# ...
# E aí Paulo vamos dar uma volta hoje?
# Se eu terminar o meu trabalho, eu consigo sair.
# ...

trabalho_terminado = False
if trabalho_terminado == True:
  print('Bora sair!!!')

else:
  print('Ainda não terminei meu trabalho.')

# Você consegue ajudar a mover essas caixas lá para fora
# Se eu estiver livre , sim. Mas, se não pede para o meu irmão para te ajudar

estou_livre = True
if estou_livre == True:
  print('Sim, posso ajudar')

else:
  print('Peça ajudar para o meu irmão')

# Eu cheguei atrasado na aula, ainda posso entrar?
# Se essa não for a sua terceira vez chegando atrasad,então pode entrar, caso contrário você irá tomar uma suspensão.

numero_de_atrasos = 3
if numero_de_atrasos >= 3:
      print('Você está suspenso')

elif numero_de_atrasos == 1:
    print('Pode entrar, mas se atrasar mais 2 vezes irá ser suspenso')

elif numero_de_atrasos == 2:
    print('Pode entrar, mas se chegar mais 1 vez atrasado vai ser suspenso')

else:
    print('Pode entrar')

# valor_salario = input("Digite o valor do seu salário: R$ ")
# horas_trabalhadas = input("Digite quantas horas você trabalha no mês: ")
# valor_hora  = int (valor_salario) /int (horas_trabalhadas)
# print("O valor por hora trabalhada é de : R$ ",valor_hora)