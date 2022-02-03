valor_fatorial = int(input('Favor digitar o valar a ser fatorado: '))
total = 1

if valor_fatorial > 0:

  for fatorial in range(1, valor_fatorial+1):
    total = int(total) * int(fatorial)

print(total)    