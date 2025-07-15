salario = float(input('Qual é o seu salário? R$'))
if salario >= 1250:
    novo_salario = salario + (salario * 10 / 100)
else:
    novo_salario = salario + (salario * 15 / 100)

print ('O seu novo salario será de R${}'.format(novo_salario))