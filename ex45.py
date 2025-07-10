import random

# jogador 
print (''' Suas opções:
      [1] Pedra
      [2] Papel
      [3] Tesoura''')

#Jogada do jogador
jogador = int(input('Qual é a sua jogada?'))

if jogador not in [1, 2, 3]:
  print('Escolha inválida! tente novamente.')
else: 
   opcao = [1, 2, 3]  # 1: Pedra, 2: Papel, 3: Tesoura


# computador
computador = random.choice(opcao) 

# Exibir jogadas
print(f'Você escolheu: {jogador}')
print(f'O computador escolheu: {computador}')

if jogador == computador: 
   resultado = print('Empate')

elif (jogador == 1 and computador == 3) or \
    (jogador == 2 and computador == 1) or \
    (jogador == 3 and computador == 2 ):
  print ('Você venceu!')
else: 
    print('O computador venceu!')