distancia = float(input('Qual a distância da sua viagem?'))
print('Você esta prestes a começar uma viagem de {}km'.format(distancia))
if distancia > 200:
    passagem = distancia * 0.45 
else: 
    passagem = distancia * 0.50
#passagem = distancia * .50 if distancia <= 200 else distancia * 0.45 #versão simplificada
print('E o preço da sua passagem será de R${}'.format(passagem))