from datetime import date 
atual = date.today().year
nascimento = int(input('Ano de nascimento:'))
idade = atual - nascimento 
print ('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print("classificação MIRIM")
elif idade <= 14:
    print("classificação INFANTIL")
elif idade  <= 19:
    print("classificação JUNIOR")
elif idade <= 25:
    print("classificação SÊNIOR")
else:
    print("classificação MASTER")