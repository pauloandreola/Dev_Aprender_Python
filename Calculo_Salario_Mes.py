valor_salario = input("Digite o valor do seu salário: R$ ")
horas_trabalhadas = input("Digite quantas horas você trabalhou esse mês: ")
valor_hora  = int (valor_salario) /int (horas_trabalhadas)
print("O valor por hora trabalhada é de : R$ ",'%.2F'%valor_hora)
