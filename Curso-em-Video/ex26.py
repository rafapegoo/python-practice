frase = str(input('Digite uma frase:')).strip().upper()
#contagem_a = frase.count('A')
print("a letra a aparece {} vezes".format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A aparece na posição'.format(frase.rfind('A')+1))
 


