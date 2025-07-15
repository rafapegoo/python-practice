from random import randint #importa biblioteca random (aleatório)
from time import sleep #importa biblioteca time
computador = randint(0,5) #faz o computador pensar
print('-=-' * 20) #decoração
print('Vou pensar em um número de 0 a 5, tente adivinhar...') 
print('-=-' * 20)
jogador = int(input('Em que número eu pensei?')) #jogador tenta divinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Parabéns, você acertou!')
else:
    print('Que pena, eu pensei no número {}, você errou!'.format(computador))



 