n= str(input("Digite seu nome completo:")).strip()
nome= n.split()
print('seu primiro nome é {}'.format(nome[0]))
print('seu ultimo nome é {}'.format(nome[len(nome)-1]))

