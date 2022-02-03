precos = [20, 50, 200]

print(precos[0])
print(precos[2])
print(precos.index(50))
# print(precos.index(310)) # Essa impressão vai gerar erro pois o valor não consta na lista
print('')

diversos = ['Paulo', 98, True]

print(diversos[0])
print(diversos[1])
print(diversos[2])
print('')

for preco in precos:
  print(preco)
print('')

for item in diversos:
  print(item)