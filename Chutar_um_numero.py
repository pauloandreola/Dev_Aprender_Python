from random import randint

numero_aleatorio = randint(1,10)
# print('Valor aleatório: ',numero_aleatorio)
numero = 0

while (numero != numero_aleatorio):

  numero = int(input('Digite um valor entre 1 e 10: '))

  if numero <= 1 or numero >= 10:

    print('Você digitou um valor diferente do solicitado')

  else: 

    if numero > numero_aleatorio:

      print('O valor digitado é maior que o valor aleatorio')

    elif numero < numero_aleatorio:

      print('O valor digitado é menor que o valor aleatorio')

    else:

      print('Você acertou o valor')